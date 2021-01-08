from django.db import models

# Create your models here.
class DisquaireProjectRestApi(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    owner = models.CharField(max_length=200,blank=False, default='')
    encoding = models.CharField(max_length=70, blank=False, default='')
    collate = models.CharField(max_length=70, blank=False, default='')
    ctype = models.CharField(max_length=70, blank=False, default='')
