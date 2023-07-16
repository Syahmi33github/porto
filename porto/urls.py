"""
URL configuration for porto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("project/", views.project),
    path("project-ds/", views.projectDS),
    path("project-cv/", views.projectCV),
    path("project-nlp/", views.projectNLP),
    path("project1/", views.project1),
    path("project2/", views.project2),
    path("project3/", views.project3),
    path("project4/", views.project4),
    path("project5/", views.project5),
    path("project6/", views.project6),
    path("project7/", views.project7),
    path("project8/", views.project8),
    path("project9/", views.project9),
    path("project10/", views.project10),
    path("admin/", admin.site.urls),
]
