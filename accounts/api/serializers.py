from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from statusapi.settings import SIMPLE_JWT

import datetime
import json

User = get_user_model()

## creating subclass to add some extra content to be sent
class MyTokenObtainPairSerailizer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user) # get refresh token by passing user instance
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token) # using refresh token to generate access token

        # Add extra responses 
        data['username'] = self.user.username
        data['expires'] = str(timezone.now() + SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])

        return data
    

        



class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    token  = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password', 
            'password2', 
            'token',
            'expires',
            ]

        extra_kwargs = {'password': {'write_only':True}}
    
    ## creating token manually to be sent on the time of registeration
    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def get_expires(self, obj):
        expires = SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        return expires

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This username already exists")
        return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This email already exists")
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')

        if pw!=pw2:
            raise serializers.ValidationError("passwords doesn;t match")
        return data

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        user_obj = User.objects.create(username=username, email=email)
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj