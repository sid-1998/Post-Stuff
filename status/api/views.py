from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from status.api.serializers import StatusSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# class ListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request, format=None):
#         qs = Status.objects.all()#it is not a error its a warning in VS code as objects member is added dynamically. if it bothers you add objects= models.Maneger() in models.py
#         serializer = StatusSerializer(data=qs, many=True)
#         serializer.is_valid()
#         return Response(serializer.data)

class StatusListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

'''
to get statuses of a particular user using its username
'''
class UserStatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    def get_queryset(self):
        kwargs = self.kwargs
        username = kwargs.get('name')# picks name from the kwargs dict passed by url
        qs = Status.objects.filter(user__username=username)## filter on the basis of name
        obj = get_list_or_404(qs)#get list of objects in queryset or raise a 404
        return obj

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer