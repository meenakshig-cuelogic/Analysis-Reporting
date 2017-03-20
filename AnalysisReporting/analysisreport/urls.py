from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [

    #url(r'^register/$',views.register,name='register'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^register/login$',views.Login ,name='login'),
 
    
]


  