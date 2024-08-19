"""demo_project URL Configuration

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
from django.urls import path
from users import views

urlpatterns = [
    path("test/", views.test_view),
    path("value-capture/<name>/<int:age>", views.value_capture_test),
    path("login/<username>/<password>", views.login),
    path("home/", views.home),
    path("value-capture-2/<name>/<int:age>", views.value_capture_test2),
    path("failure/", views.failure, name="failure"),
]
