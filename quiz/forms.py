from django.forms import  forms,ModelForm
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import User
from django import forms


class Userform(ModelForm):
    email=forms.EmailField(label='Email ID')

    class Meta:
        model=User
        fields=('username','email','password')

    def clean_email(self):
        emailid=self.cleaned_data.get('email')
        emailstatus=User.objects.filter(email=emailid)
        if emailstatus.exists():
            raise forms.ValidationError('Email is Already used')
        return emailid

class loginform(forms.Form):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)

    def clean_auth(self):
        user=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=user,password=password)

