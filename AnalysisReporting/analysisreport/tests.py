

import unittest
import os

from django.test import TestCase,Client
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory

from .views import *
from .models import *
from .forms import *


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create( username="meenakshi",email="user@mp.com", password="user")

class User_Form_Test(TestCase):

    
	def create_whatever(self):
		user=User.objects.create(username="meenakshi",email="mghamande94@gmail.com",password="As123456",password_again="As123456")
		return user
		
	def test_whatever_creation(self):
		w = self.create_whatever()
		self.assertTrue(isinstance(w))

	def test_valid_form(self):
		data = {'username': 'Abcd1234','email':'abc@gmail.com','password': 'As123456','password1':'As123456'}
		form = UserForm(data=data)
		self.assertTrue(form.is_valid())

	def test_invalid_form(self):
		w =User.objects.create(username='Mee', password='0')
		data = {'username': w.username, 'password': w.password,}
		form = UserForm(data=data)
		self.assertFalse(form.is_valid())
	
	def test_valid_login_form(self):
		data={'username':'Mee111111','password':'As123456'}
		form=LoginForm(data=data)
		self.assertTrue(form.is_valid())
	
	

	def test_whatever_list_view(self):
		w = self.create_whatever()
		url = reverse("login1")
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertIn(w.title, resp.content)

