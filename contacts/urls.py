from django.urls import path, re_path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact', views.contact, name='contact'),

]