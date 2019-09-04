from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=120, default='UNKNOWN')
    manufacturer = models.CharField(max_length=120, default='UNKNOWN')
    region = models.CharField(max_length=120, default='UNKNOWN')
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    supply = models.IntegerField(default=0)
    used = models.BooleanField(default=True)

# Create your models here.
