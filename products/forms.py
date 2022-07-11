from email.policy import default
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name", max_length=50)
    price = forms.IntegerField(label="Product Price: ")
    stocks = forms.IntegerField(label="Product Stocks: ", initial=1)