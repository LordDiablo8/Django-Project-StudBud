from django import forms
from django.forms import ModelForm
from .models import Room, User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class MyUserCreationFomr(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    

        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(self.request, "Email address already in use")
                raise ValidationError("An account with email already exists")            
            return email
        
        def clean_password1(self):
            password1 = self.cleaned_data.get("password1")

            if not any(char.isalpha() for char in password1):
                messages.error("Use alphabets in your password")
                raise ValidationError("Password must include alphabet character ")
            if not any(char.isdigit() for char in password1):
                messages.error("Use numbers in your password")
                raise ValidationError("Password must include numbers ")
            if not any(char in "!@#$%^&*()_-+=<>?/[]{}|~" for char in password1):
                messages.error("Use symbol in your password")
                raise ValidationError("Password must include a symbol ")         
            return password1

                

        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')

            if password1 and password2 and password1 != password2:
                messages.error(self.request, "Passwords do not match")
                raise forms.ValidationError("Passwords do not match")           
            return cleaned_data
        
    error_messages = {
         'password_mismatch': "The two password fields didn't match.",
    }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = {'host', 'participants'}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name', 'username', 'email', 'bio']