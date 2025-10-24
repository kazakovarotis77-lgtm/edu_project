"""First_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('first_app.urls')),
    path('course.html', TemplateView.as_view(template_name="course.html"), name='course'),  # template orqali ko'rsatish
    path('feature.html', TemplateView.as_view(template_name='feature.html'), name='feature'),
    path('testimonial.html', TemplateView.as_view(template_name='testimonial.html'), name='testimonial'),
    path('team.html', TemplateView.as_view(template_name='team.html'), name='team'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contact.html', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about.html', TemplateView.as_view(template_name='about.html'), name='about'),
    path('detail.html', TemplateView.as_view(template_name='detail.html'), name='detail'),


]



urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)