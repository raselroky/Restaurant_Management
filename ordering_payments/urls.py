from django.urls import path,include
from .import views

urlpatterns = [
    path('stripe/',views.stripe,name='stripe'),

    path('orderapil/',views.Order_Api_List.as_view()),
    path('orderapid/<int:pk>',views.Order_Api_Detail.as_view()),
    
]
