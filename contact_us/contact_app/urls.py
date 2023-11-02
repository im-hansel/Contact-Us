# contact_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks_view, name='thanks'),
]
