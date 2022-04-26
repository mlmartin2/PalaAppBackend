from rest_framework import viewsets
from .serializers import *
from ..models import *

class viewset_User(viewsets.ModelViewSet):
    serializer_class = serializer_User
    queryset = model_User.objects.all()

class viewset_SmallTask(viewsets.ModelViewSet):
    serializer_class = serializer_SmallTask
    queryset = model_SmallTask.objects.all()

