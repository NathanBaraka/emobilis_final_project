from django.shortcuts import render, redirect
from django.templatetags.static import static
from .forms import BookingForm
from .models import Booking


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def room(request):
    return render(request, 'room.html')


def booking(request):
    form = BookingForm()  # Initialize the form for GET requests

    if request.method == "POST":
        form = BookingForm(request.POST)  # Populate form with POST data
        if form.is_valid():
            print("Form is valid, saving data")
            form.save()
            return redirect('booking_success')  # Redirect to success page if form is valid
        else:
            print("Form errors:", form.errors)  # Log form errors if form is invalid

    return render(request, 'booking.html', {'form': form})  # Always pass the form to the template


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')
def booking_success(request):
    return render(request, 'booking_success.html')