from django.db import models


class Menu(models.Model):
    menu_name=models.CharField(max_length=1000,null=True,blank=True)
    price=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.menu_name
    
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=1000,null=True,blank=True)
    menu=models.ManyToManyField(Menu)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant_name
    

