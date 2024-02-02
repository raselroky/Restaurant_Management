from django.contrib import admin
from .models import Order

class Order_Column_Display(admin.ModelAdmin):
    list_display=('id','items','quantity','price')
admin.site.register(Order,Order_Column_Display)
