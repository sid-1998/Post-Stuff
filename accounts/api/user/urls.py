from django.urls import path

from .views import UserDetailAPIView
app_name = 'api-user'
urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name='detail'),
]