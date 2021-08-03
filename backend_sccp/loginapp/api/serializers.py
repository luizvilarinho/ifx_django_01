from loginapp.models import loginApp
from rest_framework import serializers


class loginAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = loginApp
        fields = ['name', 'passwd']
