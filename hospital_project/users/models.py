from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER=(
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Oher')
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.user.username + "'s Profile"

