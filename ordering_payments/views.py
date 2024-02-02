from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import filters
from .models import Order
from .serializers import Order_Serializer


def stripe(request):
    return render(request,'stripe.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context



class Order_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Order_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Order_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
class Order_Api_List(generics.ListCreateAPIView):
    search_fields=['items','quantity','price']
    filter_backends = (filters.SearchFilter,)
    queryset=Order.objects.all()
    serializer_class=Order_Serializer