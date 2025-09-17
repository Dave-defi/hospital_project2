from django.contrib import admin
from .models import *
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'specialty', 'created_on')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'phone', 'department', 'date', 'created_on')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Testimonial, TestimonialAdmin)