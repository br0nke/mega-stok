from django import forms
from .models import StockListing

class StockListingForm(forms.ModelForm):
    class Meta:
        model = StockListing
        fields = ('title', 'description', 'price', 'category', 'image', 'phone')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be positive.")
        return price

