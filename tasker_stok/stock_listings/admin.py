from django.contrib import admin
from .models import StockListing

class StockListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'price', 'image', 'phone')  # Display these fields in the list view

admin.site.register(StockListing, StockListingAdmin)
