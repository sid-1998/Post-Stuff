from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    token  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'token']

        extra_kwargs = {'password': {'write_only':True}}
    ## creating token manually to be sent on the time of registeration
    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

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