from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('doctors',views.doctors,name='doctors'),
    path('booking',views.booking,name='booking'),
]