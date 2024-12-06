from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('service/', views.service, name='service'),  # Services page
    path('room/', views.room, name='room'),  # Rooms page
    path('booking/', views.booking, name='booking'),  # Booking page
    path('team/', views.team, name='team'),  # Our Team page
    path('testimonial/', views.testimonial, name='testimonial'),  # Testimonial page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('booking_success/', views.booking_success, name='booking_success'),  # Booking success page
]
