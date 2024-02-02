from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
 
    path('api-token/login', TokenObtainPairView.as_view(), name='login-token'), #get token access for login
    path('loginapi/',views.Admin_login_Api.as_view()),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adminregisterapi/',views.Admin_Register_Api.as_view()),
    path('log-out/',views.Logout_Admin_User_Api.as_view(),name='logged-out'),


    path('updatemessageapil/',views.Update_Message_Api_List.as_view()), #create and show
    path('updatemessageapid/<int:pk>',views.Update_Message_Api_Detail.as_view()), #get,update,delete by primary key

    
]