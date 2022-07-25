from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator
from django.forms import ValidationError

from .models import Product
from .forms import ProductForm


@login_required(login_url='/login')
def index(request, id=None, page=1):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            if Product.objects.filter(name__iexact=form.cleaned_data['name']):
                error = ValidationError("Product with this name already exists.")
                form.add_error('name', error)
            
            else:
                form.save() 
                form = ProductForm()
                page = request.POST.get('page')

    elif request.method == 'GET' and id != None:
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)

    page_obj = getProducts(page=page)
    return render(request, 'products/index.html', {'products': page_obj, 'form': form, 'id': id})



def update(request, id=None, page=1):
    page_obj = getProducts(page=page)

    if id != None:
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return redirect(reverse('products_index_paged', args=[page]))

        else:
            products = Product.objects.order_by('name')
            form = ProductForm()
            return render(request, 'products/index.html', {'products': page_obj, 'form': form, 'id': id})



def delete(request, id=None, page=1):
    page_obj = getProducts(page=page)
    if id != None:
        Product(id).delete()

    return render(request, 'products/index.html', {'products': page_obj})


def getProducts(page):
    products = Product.objects.order_by('name')
    paginator = Paginator(products, 10)
    return(paginator.get_page(page))

def filter(request):
    keyword = request.POST['keyword']
    if len(keyword) > 0:
        page_obj = Product.objects.filter(name__icontains=keyword)[:10]
    else:
        page_obj = Product.objects.order_by('name   ')[:10]
    ser_page_obj = serializers.serialize('json', page_obj)
    return JsonResponse({"ser_page_obj": ser_page_obj}, status = 200)
