from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from status.api.serializers import UserStatusSerializer
from status.models import Status
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id', 
            # 'uri',
            'username',
            'email',
            'status_list',
        ]
    # def get_uri(self, user):
    #     request = self.context.get('request')
    #     return api_reverse('api-user:detail', kwargs={'username':user.username}, request=request)

    def get_status_list(self, user):
        request = self.context.get('request')
        qs = Status.objects.filter(user=user)
        return UserStatusSerializer(qs, many=True, context = {'request':request}).data