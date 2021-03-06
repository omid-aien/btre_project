from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices


# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    context = {'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices
               }
    return render(request, template_name='pages/index.html', context=context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, template_name='pages/about.html', context=context)
