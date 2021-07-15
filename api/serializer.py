from django.urls import path, include
from .models import Book, DbUModel, Course
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'description', 'time', 'school', ]


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DbUModel
        fields = ['id', 'name', 'age']


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = [Book, DbUModel, Course]
