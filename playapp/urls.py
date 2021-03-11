from django.urls import path
from django.conf.urls import url 
from .import views
from . views import index, orangecap,purplecap

#app_name= 'playapp'

urlpatterns = [
    path('',views.index , name='index'),
    path('orangecap/', views.orangecap, name='orangecap'),
    path('purplecap/',views.purplecap, name='purplecap'),
   
    
]