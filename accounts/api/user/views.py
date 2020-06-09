from django.contrib.auth import get_user_model

from rest_framework import generics

from .serializers import UserDetailSerializer
User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'