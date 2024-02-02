from django.contrib import admin
from .models import Role_And_Permission

class Role_And_Permission_Column_Display(admin.ModelAdmin):
    list_display=('id','group')
admin.site.register(Role_And_Permission,Role_And_Permission_Column_Display)