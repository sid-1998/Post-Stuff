from django.contrib.auth import get_user_model

from rest_framework import serializers

from status.api.serializers import UserStatusSerializer
from status.models import Status
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id', 
            'username',
            'email',
            'status_list',
        ]
    def get_status_list(self, user):
        qs = Status.objects.filter(user=user)
        return UserStatusSerializer(qs, many=True).data