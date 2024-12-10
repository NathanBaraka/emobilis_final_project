from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, createUserForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

def registerpage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            form.save()
            messages.success(request, 'Account created for ' + form.cleaned_data['username'])
            return redirect('login')


    context= {'form':form}
    return render(request,'register.html',context)
@unauthenticated_user
def loginpage(request):
        context= {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return redirect('login')
        return render(request,'login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def service(request):
    return render(request, 'service.html')

@login_required(login_url='login')
def room(request):
    return render(request, 'room.html')

@login_required(login_url='login')
def booking(request):
    form = BookingForm()  # Initialize the form for GET requests

    if request.method == "POST":
        form = BookingForm(request.POST)  # Populate form with POST data
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Redirect to success page if form is valid
        else:
            print("Form errors:", form.errors)  # Log form errors if form is invalid

    return render(request, 'booking.html', {'form': form})  # Always pass the form to the template

@login_required(login_url='login')
@admin_only
def booking_list(request):
    bookings = Booking.objects.all()  # Query all booking records from the database
    return render(request, 'booking_list.html', {'bookings': bookings})

@login_required(login_url='login')
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)  # Retrieve the booking instance based on the primary key

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)  # Populate form with POST data and the instance to update
        if form.is_valid():
            form.save()  # Save the updated booking
            return redirect('booking_list')  # Redirect to booking list page
    else:
        form = BookingForm(instance=booking)  # Display the current booking details in the form

    return render(request, 'booking_form.html', {'form': form})  # Render the update form template

@login_required(login_url='login')
def booking_delete_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    return render(request, 'booking_confirm_delete.html', {'booking': booking})

@login_required(login_url='login')
def team(request):
    return render(request, 'team.html')

@login_required(login_url='login')
def testimonial(request):
    return render(request, 'testimonial.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def booking_success(request):
    return render(request, 'booking_success.html')

@login_required(login_url='login')
def booking_form(request):
    return render(request, 'booking_form.html')

@login_required(login_url='login')
def booking_confirm_delete(request, booking_id):
    # Retrieve the booking object
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # If the request is a POST request, delete the booking
        booking.delete()
        # Redirect to the booking list page after deletion
        return redirect('booking_list')

    # If the request is GET, render the confirmation template
    return render(request, 'booking_confirm_delete.html', {'booking': booking})

