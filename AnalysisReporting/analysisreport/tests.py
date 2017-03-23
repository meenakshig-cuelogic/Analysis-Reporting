# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.test import TestCase

# Create your tests here.

from django.test import TestCase
 

 from .forms import *   # import all forms

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="meenakshi",email="user@mp.com", password="user")
    def user_check(self):
    	username="meenakshi"
    	

 

