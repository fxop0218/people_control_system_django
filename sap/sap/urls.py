"""sap URL Configuration

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
from django.urls import path

from personas.views import person_information, new_person, person_edit, person_delete
from webapp.views import goodbye, welcome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", welcome, name="index"),
    path("goodbye/", goodbye),
    path("person_info/<int:id>", person_information),
    path("person_edit/<int:id>", person_edit),
    path("person_delete/<int:id>", person_delete),
    path("new_person", new_person),
]
