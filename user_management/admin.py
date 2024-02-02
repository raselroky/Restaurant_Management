from django.contrib import admin
from .models import Action,Update_Message


class Action_Column_Display(admin.ModelAdmin):
    list_display=('id','actions')
admin.site.register(Action,Action_Column_Display)

class Update_Message_Column_Display(admin.ModelAdmin):
    list_display=('id','message','time')
admin.site.register(Update_Message,Update_Message_Column_Display)