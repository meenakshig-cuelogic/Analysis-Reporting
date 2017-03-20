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
	username=forms.CharField(label='username',widget=forms.TextInput(attrs={'size':'50'}))
	email= forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'size':'50'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':'50'}))
	password_again=forms.CharField(widget=forms.PasswordInput(attrs={'size':'50'}))

            
	class Meta:
		model=User
		fields=['username','email','password','password_again']
    	#email = forms.EmailField(widget=forms.TextInput(attrs={'size':'50'}))
         