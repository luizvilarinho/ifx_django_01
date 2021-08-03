from loginapp.models import loginApp
from rest_framework import viewsets
from .serializers import loginAppSerializer


class loginAppViewSet(viewsets.ModelViewSet):
    queryset = loginApp.objects.all()
    serializer_class = loginAppSerializer