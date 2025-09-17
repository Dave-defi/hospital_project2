from django.db import models

# Create your models here.

SPECIALTY = (
    ('General', 'General'),
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Neurology', 'Neurology'),
    ('Oncology', 'Oncology'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry', 'Psychiatry'),
    ('Urology', 'Urology'),
    ('Other', 'Other'),
)

DEPARTMENT = (
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Neurology', 'Neurology'),
    ('Oncology', 'Oncology'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry', 'Psychiatry'),
    ('Other', 'Other'),

)
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact Us'
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    specialty = models.CharField(choices=SPECIALTY, max_length=200, default='Other')
    
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    image = models.ImageField(upload_to='doctors_images', null=True, blank=True, default='doctor.jpg')

    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.CharField(max_length=200, choices=DEPARTMENT, default='Other')
    phone = models.CharField(max_length=100, null=True, blank=True)
    symptoms = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    testimony = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return self.name