# -*- coding: utf-8 -*-
from io import BytesIO#PARA REPORTLAB

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from apps.periodicos.models import Periodico,Origen,Ejemplar
from apps.periodicos.forms import PeriodicoForm,OrigenForm,EjemplarForm
from django.views import  View
from django.urls import reverse_lazy

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.core import serializers


from django.shortcuts import render
#Workbook nos permite crear libros en excel
from apps.fotos.pdf import Pdf, FooterCanvas

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from apps.acceso.forms import UsuarioForm

class Crearusuario(CreateView):
    model = User
    template_name="acceso/formulariocrearusuario.html"
    #form_class= UserCreationForm
    form_class= UsuarioForm
    success_url=reverse_lazy('home')
    
