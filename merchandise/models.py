from django.db import models

# Create your models here.
class Merchandise(models.Model):
    name = models.CharField(max_length=120, default='UNKNOWN')
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    supply = models.IntegerField(default=0)