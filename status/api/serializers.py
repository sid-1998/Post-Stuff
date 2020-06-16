from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from status.models import Status
from accounts.api.serializers import UserPublicSerializer




class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')#to display username instead of user id
    # user = UserPublicSerializer()
    class Meta:
        model = Status
        fields = ['id', 'uri', 'user', 'content', 'image']
        read_only_fields = ['user']


    '''
    in rest framework validate<filedname> function can be used to write 
    custom validations for every field. the arg value stores the value passed in the field.
    '''
    # def validate_content(self, value):
    #     if len(value)  < 10:
    #         raise serializers.ValidationError("Atleast write somethining dude")
    #     return value
    def get_uri(self, obj):
        return api_reverse('api-status:detail', kwargs={'pk':obj.pk}, request=self.context.get('request'))

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None

        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")

        return data
## status info to be used in userdetail page
class UserStatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'uri',
            'content',
            'image'
        ]
    def get_uri(self, obj):
        return api_reverse('api-status:detail', kwargs={'pk':obj.pk}, request=self.context.get('request'))