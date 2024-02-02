from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Restaurant,Menu
from .serializers import Restaurant_Serializer,Menu_Serializer
#from user_management.serializers import Registration_All_Serializer,Registration_All_Show_Serializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated


class Restaurant_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Restaurant.objects.get(id=pk)
        except Restaurant.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Restaurant_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Restaurant_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Restaurant_Api_List(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends = (filters.SearchFilter,)
    queryset=Restaurant.objects.all()
    serializer_class=Restaurant_Serializer


class Menu_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Menu_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Menu_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Menu_Api_List(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends = (filters.SearchFilter,)
    queryset=Menu.objects.all()
    serializer_class=Menu_Serializer