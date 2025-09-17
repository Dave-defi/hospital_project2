from django import forms
from .models import *

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Phone'}))
    # message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Message', 'rows': 3, 'class': 'form-control'}))
    
    class Meta:
        model = ContactUs
        fields = ['name', 'email','phone','message']
        widgets = {
            'message' : forms.Textarea(attrs={'placeholder': 'Enter Message', 'rows': 3, 'class': 'form-control'})
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'doctor', 'department', 'phone','symptoms', 'date']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-row form-control form-group col-lg-12'}),
            'doctor': forms.Select(attrs={'class':'form-row form-control form-group col-lg-12'}),
            'department': forms.Select(attrs={'class':'form-row form-control form-group col-lg-12'}),
            'phone': forms.NumberInput(attrs={'class':'form-row form-control form-group col-lg-12', 'placeholder': '123 456 7890'}),
            'symptoms': forms.TextInput(attrs={'class':'form-row form-control form-group col-lg-12'}),
            'date': forms.DateInput(attrs={'class':'form-row form-control form-group col-lg-12 ', 'type': 'date', 'format': '%Y-%m-%d'}),

            }