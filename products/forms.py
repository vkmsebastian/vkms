from django.forms import ModelForm, ValidationError
from products.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'stocks']

    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if Product.objects.filter(name__iexact=name):
            error = ValidationError("Product name already exists!")
            self.add_error('name', error)