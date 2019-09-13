"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .viewstotal import expedientes
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf.urls import url

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from apps.expedientes.models import Tipoexpediente,Serie
from apps.expedientes.forms import TipoExpedienteForm,SerieForm
from django.urls import reverse_lazy

#from .viewatotal import views
urlpatterns = [
    path('expediente/listar', expedientes.Listarexpediente.as_view(), name='lista_expediente'),
    path('expediente/crear', expedientes.Crearexpediente.as_view(), name='expediente-crear'),
    path('expediente/actualiza/<pk>/', expedientes.Actualizaexpediente.as_view(), name='expediente-actualiza'),
    path('expediente/elimina/<pk>/', expedientes.Eliminaexpediente.as_view(), name='expediente-eliminar'),
    
    path('tipoexpediente/listar', ListView.as_view(model=Tipoexpediente,template_name = "listartipoexpediente.html"), name='lista_tipo_expediente'),
    path('tipoexpediente/crear', CreateView.as_view(form_class= TipoExpedienteForm, template_name="expedientes/formulariotipoexpediente.html", model = Tipoexpediente), name='tipoexpediente-crear'),
    path('tipoexpediente/actualiza/<pk>/', UpdateView.as_view(form_class= TipoExpedienteForm,
        template_name="expedientes/formulariotipoexpediente.html", model = Tipoexpediente), name='tipoexpediente-actualiza'),
    path('tipoexpediente/elimina/<pk>/', expedientes.Eliminatipoexpediente.as_view(), name='tipoexpediente-eliminar'),

    path('serie/listar', ListView.as_view(model=Serie,template_name = "listarserie.html"), name='lista_serie'),
    #path('serie/crear', CreateView.as_view(form_class= SerieForm, template_name="expedientes/formularioserie.html", model = Serie), name='serie-crear'),
    path('serie/crear', expedientes.Crearserie.as_view(), name='serie-crear'),
    path('serie/actualiza/<pk>/', UpdateView.as_view(form_class= SerieForm,
        template_name="expedientes/formularioserie.html", model = Serie), name='serie-actualiza'),
    path('serie/elimina/<pk>/', expedientes.Eliminaserie.as_view(), name='serie-eliminar'),
    

]
