from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from . import models
from django.contrib import messages
from django.core.mail import send_mail
from btre.settings import EMAIL_HOST_USER

# Create your views here.


def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # check if user has made already inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = models.Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have made already inquiry for this listing')
                return HttpResponseRedirect(reverse('listings:listing', args=[listing_id]))

        cont = models.Contact(listing_id=listing_id, listing=listing, user_id=user_id, email=email, phone=phone,
                              message=message, name=name)

        cont.save()

        # Send Email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. sign into the admin panel for more info',
        #     EMAIL_HOST_USER,
        #     [realtor_email, EMAIL_HOST_USER],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return HttpResponseRedirect(reverse('listings:listing', args=[listing_id]))

