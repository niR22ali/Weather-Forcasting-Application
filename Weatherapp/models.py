from django.db import models

# Create your models here.

class thing(models.Model):
    thingName = models.CharField(max_length=50)
    thingPrice = models.IntegerField()
