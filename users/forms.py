from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # class Meta keeps configurations in one place
        model = User   # specify the Model this class will interact with (after validation this form will create new User)
        fields = ['username', 'email', 'password1', 'password2']   # fields that are going to be shown on a form


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['image']
        fields = []

