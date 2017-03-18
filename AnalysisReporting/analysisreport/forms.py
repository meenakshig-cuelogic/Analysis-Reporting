from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from analysisreport.models import Appusers


class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']