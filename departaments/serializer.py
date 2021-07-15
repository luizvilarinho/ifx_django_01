from django.urls import path, include
from .models import Company, DbDModel, Employee
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'category', 'country', 'city']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'gender', 'email', 'birth_date']


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DbDModel
        fields = ['id', 'departamento']
