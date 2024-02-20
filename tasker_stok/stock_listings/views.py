from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import StockListingForm
from django.http import HttpRequest, HttpResponse

def listing_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = StockListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('listing_detail', listing.pk)
    else:
        form = StockListingForm()
    return render(request, 'stock_listings/listing_create.html', {'form': form})

def listing_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'stock_listings/listing_list.html', {
        'listing_list': models.StockListing.objects.all(),
    })

def listing_detail(request: HttpRequest, pk) -> HttpResponse:
    return render(request, 'stock_listings/listing_detail.html', {
        'listing': get_object_or_404(models.StockListing, pk=pk),
    })