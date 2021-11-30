from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Post, UserProfile
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]

class addPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["postname", "description"]
        widgets = {
            'postname': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["birthdate", "mobileno", "gender", "city","pincode","profile","document"]
        widgets = {
            'birthdate': forms.TextInput(attrs={'class': 'form-control'}),
            'mobileno': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            #'profile' : forms.ImageField(),
        }
        