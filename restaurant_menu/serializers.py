from rest_framework import serializers
from .models import Restaurant,Menu

class Restaurant_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=('__all__')

class Menu_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=('__all__')