from time import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Product
from .forms import ProductForm

def index(request, id=None):
    products = Product.objects.order_by('name')
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('')

    elif id != None:
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        return render(request, 'products/index.html', {'products': products, 'form': form, 'id': id})
    
    return render(request, 'products/index.html', {'products': products, 'form': form})



def update(request, id=None):
    if id != None:
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
        else:
            products = Product.objects.order_by('name')
            return render(request, 'products/index.html', {'products': products, 'form': form, 'id': id})



def delete(request, id=None):
    if id != None:
        Product(id).delete()

    return HttpResponseRedirect('/products')
