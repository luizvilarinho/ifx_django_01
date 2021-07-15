from django.urls import path, include
from .models import DbDModel, Company, Employee
from rest_framework import viewsets
from .serializer import CompanySerializer, ModelSerializer, EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = DbDModel.objects.all()
    serializer_class = ModelSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
