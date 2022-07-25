from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    stocks = models.IntegerField()
    pub_date = models.DateTimeField('date published', auto_now=True)


    def __str__(self):
        return self.name