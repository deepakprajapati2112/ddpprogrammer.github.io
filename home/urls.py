from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='servicers'),
    path("contact",views.contact, name='contact'),
    path("homm",views.homm, name ='homm')
]