from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

urlpatterns = [

    path('rolesapil/',views.Role_And_Permission_Api_List.as_view()), #create and show
    path('rolesapid/<int:pk>',views.Role_And_Permission_Api_Detail.as_view()), #get,update,delete by use primary key
    path('permissionallshowapil/',views.Permission_Show_Search_Api.as_view()),
    
]