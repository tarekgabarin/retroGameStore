from django.db import models

# Create your models here.
class Customer(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=120, default='UNKNOWN')
    money = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    store_credit = models.DecimalField(decimal_places=2, max_digits=10000, default=0)