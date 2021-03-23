from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('',views.dashBoard, name='dashBoard'),
    path('loginCheck', views.loginCheck, name="loginCheck"),
    path('logout',views.logout,name='logout'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('profile',views.profile,name='profile')
]
