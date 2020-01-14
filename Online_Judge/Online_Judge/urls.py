"""Online_Judge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , re_path , include
from user import views as user_views
from problems import views as prob_views
from submission import views as sub_views

#from ckeditor_uploader import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
