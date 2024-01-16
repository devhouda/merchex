from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context={'listings': listings})

def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>55555555</p>')