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
from .viewstotal import periodicos
from django.conf.urls import url

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from apps.periodicos.models import Periodico,Origen
from apps.periodicos.forms import PeriodicoForm,OrigenForm
from django.urls import reverse_lazy

#from .viewatotal import views
urlpatterns = [
    
  
    path('periodico/listar', periodicos.Listarperiodico.as_view(), name='lista_periodico'),
    path('periodico/crear', periodicos.Crearperiodico.as_view(), name='periodico-crear'),
    path('periodico/actualiza/<pk>/', periodicos.Actualizaperiodico.as_view(), name='periodico-actualiza'),
    path('periodico/elimina/<pk>/', periodicos.Eliminaperiodico.as_view(), name='periodico-eliminar'),

    path('ejemplar/listar', periodicos.Listarejemplar.as_view(), name='lista_ejemplar'),
    path('ejemplar/crear', periodicos.Crearejemplar.as_view(), name='ejemplar-crear'),
    path('ejemplar/actualiza/<pk>/', periodicos.Actualizaejemplar.as_view(), name='ejemplar-actualiza'),
    path('ejemplar/elimina/<pk>/', periodicos.Eliminaejemplar.as_view(), name='ejemplar-eliminar'),
   
    path('origen/listar', ListView.as_view(model=Origen,template_name = "listarorigen.html"), name='lista_origen'),
    path('origen/crear', CreateView.as_view(form_class= OrigenForm, template_name="periodicos/formularioorigen.html", model =Origen), name='origen-crear'),
    path('origen/actualiza/<pk>/', UpdateView.as_view(form_class= OrigenForm,
        template_name="periodicos/formularioorigen.html", model = Origen), name='origen-actualiza'),
    path('origen/elimina/<pk>/', periodicos.Eliminaorigen.as_view(), name='origen-eliminar'),

    path('ejemplar/reporteporperiodico', periodicos.Reporteejemplarperiodico.as_view(), name='ejemplar-periodico'),
    path('ejemplar/listarfiltroe', periodicos.listarfiltros, name='listarfiltroe'),
    path('ejemplar/listartipoe', periodicos.listartipos, name='listartipoe'),
    path('ejemplar/reportepdf/<filtro>/', periodicos.ReporteejemplarperiodicoPdf.as_view(), name='reporteejemplarperiodicopdf'),
    
    

]
