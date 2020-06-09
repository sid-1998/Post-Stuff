from django.urls import path

from .views import UserDetailAPIView

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view()),
]