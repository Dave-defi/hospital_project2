from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            name = form.cleaned_data['name']
            form.save()
            # Send email notification
            subject = 'Appointment Scheduled'
            message = f'Hello {name} Your appointment has been scheduled for {date}.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [request.user.email]  

            send_mail(subject, message, from_email, to_email)

            messages.success(request, 'Appointment booked successfully')
            return redirect('home')
        else:
            form = AppointmentForm()
    else:
        form = AppointmentForm()

    return render(request, 'hospital/index.html', {'form': form})

def about(request):
    return render(request, 'hospital/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            form.save()
            # Send email notification

            subject = 'Appointment Scheduled'
            message = f'Thank you for contacting us.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]  # Assuming user's email is stored in request.user.email

            send_mail(subject, message, from_email, to_email)

            messages.success(request, 'Thank you for contacting Mico Hospital. We will get back to you soon')
            return redirect('home')
        
    else:
        form = ContactUsForm()
    return render(request, 'hospital/contact.html', {'form': form})

def doctor(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'hospital/doctor.html', context)

def testimonial(request):
    testimony = Testimonial.objects.all()
    context = {
        'testimony': testimony
    }
    return render(request, 'hospital/testimonial.html', context)

def treatment(request):
    return render(request, 'hospital/treatment.html')