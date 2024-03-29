from rest_framework import serializers
from .models import Role_And_Permission
from django.contrib.auth.models import Group, Permission,User
from django.contrib.auth.hashers import make_password

class Role_And_Permission_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Role_And_Permission
        fields=('__all__')

class Permission_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields=('id','name')
        #depth=0