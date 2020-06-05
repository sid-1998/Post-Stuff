from rest_framework import generics, mixins
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

# class StatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

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
        # request = self.request
        # username = request.GET.get('name', None)
        # if username is not None:
        #     qs = Status.objects.filter(user__username=username)
        #     return qs
        # return None

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

'''
using mixins to combine functioinalities
'''
class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)#builtin method in CreateModelMixin to create and save new model instance


# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

''' 
DRF provides a built-in generic view called RetrieveUpdateDestryAPIView to do the same
'''
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


'''
one view to do all
'''


class OneForALL(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    def get_queryset(self):
        request = self.request
        ## check if user has passed username parameter to filter stuff of a particular user
        username = request.GET.get('name', None)
        if username is not None:
            qs = Status.objects.filter(user__username=username)
            return qs
        return Status.objects.all()

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        obj = get_object_or_404(Status, id=passed_id)
        self.check_object_permissions(request, obj)
        return obj
    # list and retrieve
    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(self, request, *args, **kwargs)# if id is passed call retrieve to get the specific object

        return super().get(request, *args, **kwargs)#if no id is passed call the default get method of ListAPIView class
    # create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)