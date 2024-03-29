from django.db import models
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


PAY_TERM=(
    ('Select','Select'),
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Half of Month','Half of Month'),
    ('Monthly','Monthly'),
    ('Half of Year','Half of Year'),
    ('Yearly','Yearly')
)
ACTION=(
    ('Select','Select'),
    ('View','View'),
    ('Edit','Edit'),
    ('Delete','Delete')
)

    
class Action(models.Model):
    actions=models.CharField(max_length=1000,choices=ACTION,default='Select')


class Update_Message(models.Model):
    message=models.TextField(null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

