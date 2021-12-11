from django.db import models
# Create your models here.

class restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=50, null=False)
    description = models.TextField()