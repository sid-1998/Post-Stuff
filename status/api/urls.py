from django.contrib import admin
from django.urls import path
from status.api.views import StatusListAPIView

urlpatterns = [
    path('', StatusListAPIView.as_view())
]