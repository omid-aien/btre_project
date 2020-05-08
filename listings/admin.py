from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Listing)
class AdminListing(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'zipcode','list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    search_fields = ('title', 'address', 'zipcode', 'state', 'city', 'price', 'description')
    list_per_page = 25
