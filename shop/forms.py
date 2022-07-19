from django import forms
from .models import Product, Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            if visible.name == 'city':
                visible.field.widget.attrs['class'] = 'country_select'
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['onfocus'] = "this.placeholder = ''"
            visible.field.widget.attrs['onblur'] = f"this.placeholder = '{visible.name.title()}'"
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
