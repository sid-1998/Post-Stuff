from django.contrib import admin
from django.urls import path
from status.api.views import StatusListAPIView, StatusCreateAPIView, StatusDetailAPIView, UserStatusAPIView



urlpatterns = [
    path('', StatusListAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    path('<int:pk>/', StatusDetailAPIView.as_view()),
    path('<str:name>', UserStatusAPIView.as_view())

]