from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Role_And_Permission
from .serializers import Role_And_Permission_Serializer,Permission_Serializer
from django.contrib.auth.models import Group, Permission,User
#from user_management.serializers import Registration_All_Serializer,Registration_All_Show_Serializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class Role_And_Permission_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Role_And_Permission.objects.get(id=pk)
        except Role_And_Permission.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Role_And_Permission_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Role_And_Permission_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Role_And_Permission_Api_List(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends = (filters.SearchFilter,)
    queryset=Role_And_Permission.objects.all()
    serializer_class=Role_And_Permission_Serializer

class Permission_Show_Search_Api(generics.ListAPIView):
    search_fields=['id','codename','name']
    filter_backends=(filters.SearchFilter,)
    
    queryset=Permission.objects.all()
    serializer_class=Permission_Serializer