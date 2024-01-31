from django.urls import path
from . import views 
from .views import signup, display_users


urlpatterns = [
    path('', signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logouut, name='logouut'),
    path('users/', display_users, name='display_users'),
]