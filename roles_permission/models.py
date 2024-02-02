from django.db import models
from django.contrib.auth.models import Group, Permission
from django.conf import settings


class Role_And_Permission(models.Model):
    #role=models.CharField(max_length=1000,null=True,blank=True)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    permission=models.ManyToManyField(Permission,blank=True)

    def __str__(self):
        return self.group.name
