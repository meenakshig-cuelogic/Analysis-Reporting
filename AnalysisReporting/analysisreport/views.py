import uuid
import hashlib
import os
import json
from datetime import datetime
from datetime import datetime, timedelta

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
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from analysisreport.forms import *
from analysisreport.csvreader import *
from analysisreport.models import *

from django.http import Http404

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
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    
                    u1=User.objects.create_user(username,email,password)
                    user=authenticate(username=username,password=password)

                    user.is_active=False
                    user.save()
                    self.hash1=str(uuid.uuid1())
                    e1=u1.emailverify_set.create(hashkey=self.hash1)
                    subject="iCanny Account Verification"
                    from_email=settings.EMAIL_HOST_USER
                    to_list=[user.email]
                    send_mail(subject,'Dear %s, \n\nOne more step to go\nWe just need to verify your email address to complete your signup process.\nYou can activate your account by visiting below link.: http://172.21.32.80:8000/analysisreport/email_verification/?uid=%s \n\n\nThanks for your cooperation\nTeam iCanny'%(username,self.hash1),from_email,to_list,fail_silently=True)
                    messages.success(request, ' Email verification link has been sent to registered mail')
                    return render(request,self.template_name,{'form':form,'username':username})                    
                
                else:
                    messages.warning(request, 'Email is already in use')
                    return render(request,self.template_name,{'form': form})
                    
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
                return render(request,"analysisreport/loginpage.html/",{'form':form})
            else:
               return render(request,"analysisreport/loginpage.html/",{'form':form})
   
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
                        
                        return redirect('analysisreport/import_file/',{'username':username})
                    else:
                        messages.warning(request, "please verify your email")
                        return render(request,"analysisreport/loginpage.html",{'form':form,'username':username})
                else:
                    user = User.objects.filter(username=username, password=password)
                    if user.count():
                        user = user[0]
                        if user.is_active:
                            messages.warning(request,"User does not exists")
                        else:
                            messages.warning(request,"This account is not activated yet, to activate your account click verifiaction link sent to associated email address.")
                    else:       
                        messages.warning(request,"Username password combination does not match")
                return render(request,"analysisreport/loginpage.html",{'form':form,'username':username})
                    
        return render(request,"analysisreport/loginpage.html",{'form':form,'username':username})   

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
    return redirect('http://'+settings.HOST+'/analysisreport/landpage/login1/?verified=1',{'username':username} )
    

@login_required(login_url='/login1/')
def import_file(request):
    form = UploadFileForm()
    username=request.user.username

    return render(request,'analysisreport/import_file.html', {'upload_success':False, 'form': form,'username':username})

@login_required(login_url='/login1/')
def get_file_data(request):
   
    
    username=request.user.username
    outer_list=[]
    csv_headers = []

    if request.method == "POST":
        # print request.body
              
        if len(request.FILES):
            system_file_name=request.FILES['uploaded_file']
            uploaded_file_name = handle_uploaded_file(request.FILES['uploaded_file'])
            csv_headers=csv_file_header(uploaded_file_name)  
            main_list=csv_file_reader(uploaded_file_name)
            saving_list=csv_header_content(uploaded_file_name)
            for i in range(len(main_list)):
                outer_list.append(main_list[i])
            
            request.session['form_data'] = saving_list
            if(uploaded_file_name):
                messages.success(request,"File has been uploaded successfully")        
    

    return render(request, 'analysisreport/import_file.html',{'outer_list':outer_list, 'csv_headers':csv_headers, 'upload_success':True,'username':username,'system_file_name':system_file_name})


# def import_file(request):
        
#         if request.method == 'POST':
#             outer_list=[]
#             if len(request.FILES):
#                 uploaded_file_name = handle_uploaded_file(request.FILES['uploaded_file'])                
#                 csv_headers=csv_file_header(uploaded_file_name)  
#                 main_list=csv_file_reader(uploaded_file_name)
#                 for i in range(len(main_list)):
#                     outer_list.append(main_list[i])
                
#                 return render(request,'analysisreport/import_file.html',{'csv_headers':csv_headers,'outer_list': outer_list})
#         else:
#             form = UploadFileForm()
#         return render(request, 'analysisreport/import_file.html', {'form': form})



@login_required(login_url='/login1/')
def save_file(request):
    username=request.user.username
    if request.method == 'POST':
        print request.session
        user=User.objects.get(username=request.user.username) 
        user_id=request.user.id
        file_name=request.POST['userfilename']
        file_data = request.session['form_data']
        u1=Document(username=user,docfile=file_name,file_data=file_data)
        if(file_name):
            if(Document.objects.filter(docfile=file_name).exists()):
                messages.success(request,"Database name can not be same as previously saved database, please choose an unique name.")
            else:
                u1.save()
                messages.success(request,"File has been saved successfully")

        else:
            messages.warning(request,"Please select a file.")    

    return render(request,'analysisreport/import_file.html',{'filename':file_name,'user_id':user_id,'file_data':file_data,'username':username})


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
