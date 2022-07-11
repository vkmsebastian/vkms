from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stocks = models.IntegerField(default=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name