from django.urls import path

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterAPIView, MyTokenObtainPairView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view())
]