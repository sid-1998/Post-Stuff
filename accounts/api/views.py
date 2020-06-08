from django.contrib.auth import get_user_model

from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegisterSerializer, MyTokenObtainPairSerailizer
from .permissions import AnonPermissionOnly

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerailizer

class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [AnonPermissionOnly]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer