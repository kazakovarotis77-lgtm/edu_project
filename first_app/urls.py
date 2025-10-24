from django.urls import path
from .views import home, Salom_Detail  
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    path('', home, name='home'),
    path('name/<int:pk>/', Salom_Detail.as_view(), name='viki_detail'),  
    path('course.html/', lambda request: render(request, 'course.html'), name='course'),

]
