
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('restaurantapil/', views.Restaurant_Api_List.as_view()), #create and show 
    path('restaurantapid/<int:pk>', views.Restaurant_Api_Detail.as_view()), #get,update,delete by use primary key

    path('menuapil/', views.Menu_Api_List.as_view()), #create and show 
    path('menuapid/<int:pk>', views.Menu_Api_Detail.as_view()), #get,update,delete by use primary key


]
