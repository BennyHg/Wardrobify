from django.db import models
from django.urls import reverse

class Hat(models.Model):
    name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    picture_url = models.URLField(null=True)

    