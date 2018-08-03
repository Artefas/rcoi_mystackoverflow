from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user_id = models.IntegerField(primary_key=True)
    about   = models.CharField(max_length=256, default=None, null=True)
    url_facebook = models.CharField(max_length=128, default=None, null=True)
    url_vk       = models.CharField(max_length=128, default=None, null=True)
    url_twitter  = models.CharField(max_length=128, default=None, null=True)
    url_github   = models.CharField(max_length=128, default=None, null=True)
    rating  = models.PositiveIntegerField(default=0)
    registration_date = models.DateField(auto_now_add=True)

