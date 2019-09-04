from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=120, default='UNKNOWN')
    publisher = models.CharField(max_length=120, default='UNKNOWN')
    console = models.CharField(max_length=120, default='UNKNOWN')
    region = models.CharField(max_length=120, default='UNKNOWN')
    genre = models.CharField(max_length=120, default='UNKNOWN')
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    supply = models.IntegerField(default=0)
    used = models.BooleanField(default=True)
    ersb = models.CharField(max_length=120, default='UNKNOWN')

