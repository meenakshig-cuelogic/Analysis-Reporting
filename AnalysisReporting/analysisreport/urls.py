from django.conf.urls import url
from analysisreport import views
from . import forms
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [

    #url(r'^register/$',views.register,name='register'),
    url(r'^landpage/$',views.landpage,name='landpage'),
    
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    
    url(r'^landpage/register/$',views.UserFormView.as_view(),name='register'),
   
   url(r'^landpage/register/analysisreport/landpage$',views.landpage,name='landpage'),

   url(r'^landpage/login1/analysisreport/landpage$',views.landpage,name='landpage'),

   url(r'^landpage/login1/analysisreport/Login$',views.login1,name='login'),

    
    url(r'^landpage/login1/$',views.login1,name='login'),

    url(r'^landpage/register/Login$',views.login1,name='login'),

    url(r'^landpage/login1/analysisreport/register$',views.UserFormView.as_view(),name='register'),
        
    url(r'^landpage/register/analysisreport/register$',views.UserFormView.as_view(),name='register'),
      

    url(r'^register/Login/$',views.Login, name='Login'),
 	
 	url(r'^landpage/login/$', auth_views.login, {'template_name': 'analysisreport/loginpage.html'}, name='login'),
 	
    url(r'^login/$', auth_views.login, {'template_name': 'analysisreport/loginpage.html'}, name='login'),
 	
    url(r'^email_verification/$', views.email_verification,name='email_verification'),
 	
 	url(r'^$', TemplateView.as_view(template_name='analysisreport/home.html'), name='home'),
	
	url(r'^register/login/$', auth_views.login, {'template_name': 'analysisreport/loginpage.html'}, name='login'),
 	
 	url(r'^email_verification/login1/$',views.login1,name='login1'),
	]
