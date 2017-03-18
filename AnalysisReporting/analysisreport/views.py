from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from django.views.generic import View
from analysisreport.forms import UserForm
from django.core.exceptions import ObjectDoesNotExist
 
 
class UserFormView(View):


    form_class=UserForm
    template_name='analysisreport/registration_form.html'

    def home(request):
        return render(request, 'analysisreport/home.html')


    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form': form})


    def post(self,request):

        if request.method=='POST':
            form=self.form_class(request.POST)
            if form.is_valid():
                
                username=form.cleaned_data['Username']
                password=form.cleaned_data['password1']
                email=form.cleaned_data['e_mail']
                if not (User.objects.filter(username=username).exists() or User.objects.filter(username=username).exists()):
                    User.objects.create_user(username,email,password)
                      
                     
                    user=authenticate(username=Username,password=password)
                    login(request,user)
                    form.save()
                    subject="hello account creation successful"
                    message=" click the link below to login %s"%url, 
                    from_email=settings.EMAIL_HOST_USER
                    to_list=[User.email]
                    send_mail(subject,message,from_email,to_list,fail_silently=true)
                    
                    return HttpResponse("/")
                     
             
                else:
                    return HttpResponse("already exists")
        return render(request,self.template_name,{'form': form}) 
    
def login(request):
        form=UserForm(None)
        return render(request,'analysisreport/loginpage.html',{'form': form}) 
   


            
 