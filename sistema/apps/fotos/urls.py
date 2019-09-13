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
from .viewstotal import fotos
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf.urls import url

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from apps.fotos.models import Tipofoto,Procedencia
from apps.fotos.forms import TipoFotoForm,ProcedenciaForm
from django.urls import reverse_lazy

#from .viewatotal import views
urlpatterns = [
    
  
    path('', LoginView.as_view(template_name='index.html'), name="login"),
    path('registro/password_reset/',
        PasswordResetView.as_view(template_name='registro/password_reset_form.html',
            email_template_name='registro/password_reset_email.html'),
        name='password_reset'
    ),
    path('registro/password_reset_done/',
        PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset1/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'),
        name='password_reset_confirm1'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'),
     name='password_reset_complete'),
    path('foto/home', fotos.Home.as_view(), name='home'),
    path('foto/listar', fotos.Listar.as_view(), name='listar'),
    path('foto/crear', fotos.Crearfoto.as_view(), name='foto-crear'),
    path('foto/actualiza/<pk>/', fotos.Actualizafoto.as_view(), name='foto-actualiza'),
    path('foto/elimina/<pk>/', fotos.Eliminafoto.as_view(), name='foto-eliminar'),
    path('foto/reporte', fotos.Reportefoto.as_view(), name='foto-reporte'),
    path('foto/listarfiltro', fotos.listarfiltros, name='listarfiltro'),
    path('foto/listartipo', fotos.listartipos, name='listartipo'),
    path('foto/reportefototipo', fotos.Reportefototipo.as_view(), name='foto-tipo'),
    path('foto/listarpdf', fotos.Listar.pdf_Platypus, name='listarpdf'),
    path('foto/upload', fotos.upload_image_view, name='upload_image_view'),
    #path('foto/reportepdf/<filtro>/', fotos.Reportefototipo.pdf_Platypus, name='reportepdf'),
    path('foto/reportepdf/<filtro>/', fotos.FotoportipoPdf.as_view(), name='reportepdf'),
    #path('foto/reportepdf/<filtro>/', fotos.Pdf.as_view(), name='reportepdf'),
    #path('foto/reportepdf/<filtro>/', fotos.Reportefototipo.pdf_Platypus, name='reportepdf'),

    path('foto/reporte_fotos_excel/<filtro>/', fotos.ReporteFotosExcel.excel_openpyxl, name="reporte_fotos_excel"),
    #url(r'^foto/reporte_fotos_excel/(\w+)/$', fotos.ReporteFotosExcel.as_view(), name="reporte_fotos_excel"),
    path('tipofoto/listar', ListView.as_view(model=Tipofoto,template_name = "listartipo.html"), name='lista_tipo_foto'),
    path('tipofoto/crear', CreateView.as_view(form_class= TipoFotoForm, template_name="fotos/formulariotipofoto.html", model = Tipofoto), name='tipofoto-crear'),
    path('tipofoto/actualiza/<pk>/', UpdateView.as_view(form_class= TipoFotoForm,
        template_name="fotos/formulariotipofoto.html", model = Tipofoto), name='tipofoto-actualiza'),
    path('tipofoto/elimina/<pk>/', fotos.Eliminatipofoto.as_view(), name='tipofoto-eliminar'),

    path('procedencia/listar', ListView.as_view(model=Procedencia,template_name = "listarprocedencia.html"), name='lista_procedencia'),
    path('procedencia/crear', CreateView.as_view(form_class= ProcedenciaForm, template_name="fotos/formularioprocedencia.html", model = Procedencia), name='procedencia-crear'),
    path('procedencia/actualiza/<pk>/', UpdateView.as_view(form_class= ProcedenciaForm,
        template_name="fotos/formularioprocedencia.html", model = Procedencia), name='procedencia-actualiza'),
    path('procedencia/elimina/<pk>/', fotos.Eliminaprocedencia.as_view(), name='procedencia-eliminar'),
    

]
