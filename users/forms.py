from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

""" I have defined a new form class and passed the userCreation for to it"""
class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=64)
    last_name=forms.CharField(max_length=64)
    email=forms.EmailField(max_length=254)

    """ class meta allows me to define the model I 
    want the changes to happen on, which in this case is the User model
    lastle, I defined fields which tells dango in which order I would like to 
    form labels to appear on the registration page """

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
  


