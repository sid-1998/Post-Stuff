from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']


    '''
    in rest framework validate<filedname> function can be used to write 
    custom validations for every field. the arg value stores the value passed in the field.
    '''
    # def validate_content(self, value):
    #     if len(value)  < 10:
    #         raise serializers.ValidationError("Atleast write somethining dude")
    #     return value
    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None

        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")

        return data