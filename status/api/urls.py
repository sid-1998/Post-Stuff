
from django.urls import path
from status.api.views import (
    StatusAPIView,
    StatusDetailAPIView, 
    OneForALL
                            )


app_name = 'api-status'
urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:pk>/', StatusDetailAPIView.as_view(), name='detail'),
    # path('', StatusListAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),

    # path('', OneForALL.as_view()),
    # path('<str:name>/', UserStatusAPIView.as_view()),

]