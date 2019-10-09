from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import  Textarea,Select
from .models import Profile

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
     email=forms.EmailField()
 
     class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['image','bio']
        widgets = {
                
            'bio': Textarea(attrs={'cols': 20, 'rows': 5,'class':'form-control'})
            
        }