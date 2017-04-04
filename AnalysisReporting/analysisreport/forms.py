from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.forms import ModelForm
from django import forms

 


class UserForm(forms.ModelForm):
	username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'size':'50','placeholder':'Username'}))
	email= forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'size':'50','placeholder':'email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':'50','placeholder':'password'}))
	password_again=forms.CharField(widget=forms.PasswordInput(attrs={'size':'50','placeholder':'retype password'}))

            
	class Meta:
		model=User
		fields=['username','email','password','password_again']
    	 
class LoginForm(forms.Form):

    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'size':'50','placeholder': 'Enter Email address'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'size':'50','placeholder': 'Enter Password'}))
        