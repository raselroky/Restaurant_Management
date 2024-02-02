from django.db import models

class Order(models.Model):
    items=models.CharField(max_length=1000,null=True,blank=True)
    quantity=models.TextField(null=True,blank=True)
    price=models.TextField(null=True,blank=True)
    