from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Realtor)
class AdminListing(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'hire_date')
    list_per_page = 25
    search_fields = ('name', 'phone', 'description')
