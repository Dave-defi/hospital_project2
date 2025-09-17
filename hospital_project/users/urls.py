from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),

    path('sign-in/', views.signin, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),

    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),

    

]
