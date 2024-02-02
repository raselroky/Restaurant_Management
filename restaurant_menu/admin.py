from django.contrib import admin
from .models import Restaurant,Menu

class Restaurant_Column_Display(admin.ModelAdmin):
    list_display=('id','restaurant_name','get_menu','date_time')

    def get_menu(self, obj):
        return "\n".join([p.menu for p in obj.menu.all()])

admin.site.register(Restaurant,Restaurant_Column_Display)

class Menu_Column_Display(admin.ModelAdmin):
    list_display=('id','menu_name','price')
admin.site.register(Menu,Menu_Column_Display)
