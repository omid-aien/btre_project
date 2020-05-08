from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from . import models
from .choices import state_choices, bedroom_choices, price_choices

# Create your views here.


def index(request):
    listings = models.Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {'listings': page_listings}
    return render(request, template_name='listings/listings.html', context=context)


def listing(request, listing_id):
    listing = get_object_or_404(models.Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, template_name='listings/listing.html', context=context)


def search(request):

    query_listings = models.Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listings = query_listings.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listings = query_listings.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_listings = query_listings.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listings = query_listings.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_listings = query_listings.filter(price__lte=price)

    context = {'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices,
               'listings': query_listings,
               'values': request.GET
               }
    return render(request, template_name='listings/search.html', context=context)
