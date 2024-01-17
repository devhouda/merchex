from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', context={'band': band})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', context={'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', context={'listing': listing})


def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>55555555</p>')