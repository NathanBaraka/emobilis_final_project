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
    path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('booking_update/<int:pk>/', views.booking_update, name='booking_update'),  # Add this line
    path('booking_delete/<int:booking_id>/', views.booking_confirm_delete, name='booking_confirm_delete'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
