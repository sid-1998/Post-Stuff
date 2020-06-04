from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from status.api.serializers import StatusSerializer

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

