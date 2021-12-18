from django import forms
from .models import OrderItem, ColourVariation, Product, SizeVariation


class AddToCartForm(forms.ModelForm):
    colour = forms.ModelChoiceField(queryset=ColourVariation.objects.none())
    size = forms.ModelChoiceField(queryset=SizeVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'colour', 'size']

    def __init__(self, *args, **kwargs):
        produt_id = kwargs.pop('product_id')
        product = Product.objects.get(id=produt_id)
        super().__init__(*args, **kwargs)
        self.fields['colour'].queryset = product.available_colour.all()
        self.fields['size'].queryset = product.available_size.all()
