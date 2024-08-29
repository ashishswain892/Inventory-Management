from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'product_id' : 'Product ID',
            'name' : 'Name',
            'stock_keep_unit' : 'Stock_keep_unit',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g 1', 'class':'forms-control'}),
             'name': forms.TextInput(
                attrs={'placeholder':'e.g shirt', 'class':'forms-control'}),
             'stock_keep_unit': forms.TextInput(
                attrs={'placeholder':'e.g S1234', 'class':'forms-control'}),
             'price': forms.NumberInput(
                attrs={'placeholder':'e.g 500.00', 'class':'forms-control'}),
             'quantity': forms.NumberInput(
                attrs={'placeholder':'e.g 10', 'class':'forms-control'}),
             'supplier': forms.TextInput(
                attrs={'placeholder':'e.g ABC corp', 'class':'forms-control'}),
                
        }
