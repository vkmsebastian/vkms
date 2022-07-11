from time import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Product
from .forms import ProductForm

def index(request, id=None):
    products = Product.objects.order_by('name')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            stocks = form.cleaned_data['stocks']
            pub_date = timezone.now()
            Product(name=name, price=price, stocks=stocks, pub_date=pub_date).save()
        
        return HttpResponseRedirect('')

    else:
         if id != None:
            products = Product.objects.order_by('name')
            product = Product.objects.get(id=id)
            print(request.method)
            # return HttpResponseRedirect('/products', {'products': products, 'product':product})
            return render(request, 'products/index.html', {'products': products, 'product':product})

    return render(request, 'products/index.html', {'products': products})
