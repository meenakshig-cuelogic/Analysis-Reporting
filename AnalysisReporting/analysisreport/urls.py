from django.conf.urls import url
from . import views

urlpatterns = [

     
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^register/login$',views.login ,name='login'),
 
    
]


  