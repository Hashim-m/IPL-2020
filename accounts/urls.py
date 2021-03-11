from django.urls import path

from .import views
from . views import register,login,logout

urlpatterns = [
    path('register',views.register , name='register'),
    path('login',views.login ,name='login'),
    path('logout',views.logout ,name='logout'),
   
    ]