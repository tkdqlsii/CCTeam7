from django.db import models

# Create your models here.
class MelonChart(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
