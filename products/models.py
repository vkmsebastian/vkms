from pydoc import stripid
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.CharField(max_length=4)
    stocks = models.CharField(max_length=4)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.name