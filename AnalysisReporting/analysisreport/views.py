import uuid
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from django.contrib.auth.views import login 
from django.views.generic import View
from analysisreport.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from analysisreport.models import *
from datetime import datetime
from datetime import datetime, timedelta
from django.utils import timezone
import hashlib
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from analysisreport.csvreader import csv_file_reader


class UserFormView(View):

     
    form_class=UserForm
    template_name='analysisreport/registration_form.html'
    uid='null';
    def home(request):
        return render(request, 'analysisreport/home.html')


    def get(self,request):
        form=self.form_class(request.POST)
        return render(request,self.template_name,{'form': form})


    def post(self,request): 
        if request.method =='POST':
            form=self.form_class(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                if not (User.objects.filter(username=username).exists() or User.objects.filter(username=username).exists()):
                    
                    u1=User.objects.create_user(username,email,password)
                    user=authenticate(username=username,password=password)

                    user.is_active=False
                    user.save()
                    self.hash1=str(uuid.uuid1())
                    e1=u1.emailverify_set.create(hashkey=self.hash1)
                    subject="Welcome Account Creation Successful!!!!!"
                    from_email=settings.EMAIL_HOST_USER
                    to_list=[user.email]
                    send_mail(subject,'please click the given link to log in: http://172.21.32.80:8000/analysisreport/email_verification/?uid=%s'%(self.hash1),from_email,to_list,fail_silently=True)
                    messages.success(request, ' email verification link has been sent to registered mail')
                    return render(request,'analysisreport/email.html',{'form':form})                    
                else:
                    return HttpResponse("failed")
                    
        messages.warning(request, 'Username is already in use')
        return render(request,self.template_name,{'form': form})

def Login(request):
        form=UserForm(None)
        messages.warning(request, 'YOU HAVENT VERIFIED EMAIL YET')
        return render(request,'analysisreport/loginpage.html',{'form': form}) 
   
def forgotpass(request):
        form=UserForm(None)
        return render(request,'analysisreport/forgotpassword.html',{'form': form}) 
   
def landpage(request):
        form=UserForm(None)
        return render(request,'analysisreport/landingpage.html',{'form': form}) 

def home(request):
    form=LoginForm()
    return render(request,'analysisreport/home.html',{'form': form})
            
def login1(request):
    verf_value=request.GET.get('verified',None)
    if request.method == 'GET':
            form = LoginForm()
            if verf_value:
                messages.success(request, "Your account has been successfully verified, now you can login.")
                return render(request,"analysisreport/loginpage.html",{'form':form})
            else:
               # messages.success(request, "make sure you have a activated account")
                return render(request,"analysisreport/loginpage.html",{'form':form})
   
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): 
                username=form.data.get('username')
                password=form.data.get('password')
                user=authenticate(username=username,password=password)
                print user
                if user is not None:

                    if user.is_active:
                        login(request,user)
                        return redirect('/analysisreport/import_file')
                    else:
                        messages.warning(request, "please verify your email")
                else:
                    user = User.objects.filter(username=username, password=password)
                    if user.count():
                        user = user[0]
                        if user.is_active:
                            messages.warning(request,"User does not exists")
                        else:
                            messages.warning(request,"This account is not activated yet, to activate your account click vitrifaction link sent to associated email address.")
                    else:       
                        messages.warning(request,"Username password combination does not match")
                return render(request,"analysisreport/loginpage.html",{'form':form})
                    
        return render(request,"analysisreport/loginpage.html",{'form':form})   

def email_verification(request):
    form = LoginForm()
    hash1=request.GET.get('uid', '')
    if (hash1):
        emailverify_obj=emailverify.objects.get(hashkey=hash1)
    else:
        raise ValueError('incorrect hashkey')
    time_date=emailverify_obj.Reg_time
    if time_date < (timezone.now() - timedelta(hours=24)):
        raise ValidationError('LinkExpired try one go for registration')
    username=User.objects.get(id=emailverify_obj.username.id)
    username.is_active=True
    username.save()
    return redirect('http://'+settings.HOST+'/analysisreport/landpage/login1/?verified=1', )
    

def import_file(request):
        
        if request.method == 'POST':
             
            if len(request.FILES):
                uploaded_file_name = handle_uploaded_file(request.FILES['uploaded_file'])                
                u1=User.objects.filter(username=request.user.username)  
                main_list=csv_file_reader(uploaded_file_name)
                return render(request,'analysisreport/import_file.html',{'main_list': main_list})
        else:
            form = UploadFileForm()
        return render(request, 'analysisreport/import_file.html', {'form': form})
        
def c_analysis(request):
    form=LoginForm()
    return render(request,'analysisreport/c_analysis.html',{'form': form})
def d_analysis(request):
    form=LoginForm()
    return render(request,'analysisreport/d_analysis.html',{'form': form})
def report(request):
    form=LoginForm()
    return render(request,'analysisreport/repot.html',{'form': form})

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    new_file = open(file_path, 'wb+')
    new_file.write(f.read())
    return file_path