from loginapp.models import loginApp
from rest_framework import viewsets
from .serializers import loginAppSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class loginAppViewSet(viewsets.ViewSet):

    def list(self, request):
        print("GEEET")
        queryset = loginApp.objects.all()
        serializer = loginAppSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
        
    queryset = loginApp.objects.all()
    serializer_class = loginAppSerializer
