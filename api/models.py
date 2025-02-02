from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class Person(models.Model):

    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)