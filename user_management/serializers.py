from rest_framework import serializers
from .models import Action,Update_Message
from django.contrib.auth.models import Group, Permission,User
from django.contrib.auth.hashers import make_password


class Action_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Action
        fields=('__all__')



class Update_Message_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Update_Message
        fields=('__all__')

class User_Serializer(serializers.ModelSerializer):
    
    #confirmed_password=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=('username','email','password')
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
            user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])

            return user