from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Action,Update_Message
from .serializers import Action_Serializer,Update_Message_Serializer,User_Serializer
from django.contrib.auth.models import Group, Permission,User
#from user_management.serializers import Registration_All_Serializer,Registration_All_Show_Serializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


class Update_Message_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Update_Message.objects.get(id=pk)
        except Update_Message.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Update_Message_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Update_Message_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Update_Message_Api_List(generics.ListCreateAPIView):
    search_fields=['id','message','time']
    filter_backends=(filters.SearchFilter,)
    queryset=Update_Message.objects.all()
    serializer_class=Update_Message_Serializer


class Admin_Register_Api(APIView):
    def post(self,request):
        serializer=User_Serializer(data=request.data)
        data={}
        if(serializer.is_valid()):
            account=serializer.save()

            data['response']="your account has been created"
            data['username']=account.username
            data['email']=account.email
            data['password']=account.password

            token=Token.objects.get(user=account).key
            data['token']=token

            return Response(data)
        return Response(serializer.errors)

class Admin_login_Api(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=User.objects.all()
    serializer_class=User_Serializer
    


class Logout_Admin_User_Api(APIView):
    def post(request):

        if(request.user.auth_token.delete()):

            return Response({"Message":"You are logged Out"},status=status.HTTP_200_OK)
        return Response({"Message":"Auth has no attribute"})