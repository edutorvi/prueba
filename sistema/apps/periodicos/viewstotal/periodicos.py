# -*- coding: utf-8 -*-
from io import BytesIO#PARA REPORTLAB

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from apps.periodicos.models import Periodico,Origen,Ejemplar
from apps.periodicos.forms import PeriodicoForm,OrigenForm,EjemplarForm
from django.views import  View
from django.urls import reverse_lazy

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet#estilosparrafo
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
#Librerias reportlab a usar:
from reportlab.platypus import (BaseDocTemplate, Frame,  
					NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.units import mm
from reportlab.platypus import Image
from reportlab.platypus.flowables import Spacer



from django.shortcuts import render
#Workbook nos permite crear libros en excel
from openpyxl import Workbook
from django.http import HttpResponseRedirect
import os

from apps.fotos.pdf import Pdf, FooterCanvas

class FooterCanvas(canvas.Canvas):

	def __init__(self, *args, **kwargs):
		canvas.Canvas.__init__(self, *args, **kwargs)
		self.pages = []

	def showPage(self):
		self.pages.append(dict(self.__dict__))
		self._startPage()

	def save(self):
		page_count = len(self.pages)
		for page in self.pages:
			self.__dict__.update(page)
			self.draw_canvas(page_count)
			canvas.Canvas.showPage(self)
		canvas.Canvas.save(self)

	def draw_canvas(self, page_count):
		page1 = "Pág %s de %s" % (self._pageNumber, page_count)
		page2 = "Gobierno Regional de Cajamarca"
		x1 = 128
		x2 = 500
		x2 = 461
		self.saveState()
		self.setStrokeColorRGB(0, 0, 0)
		self.setLineWidth(0.5)
		self.line(66, 71, A4[0] - 66, 71)#linea footer
		self.setFont('Times-Roman', 10)
		self.drawString(A4[0]-x1, 59, page1)#texto footer
		
		self.setFont('Times-Roman', 12)
		self.drawString(A4[0]-x2, 785, page2)#texto cabecera
		self.line(66, 780, A4[0] - 66, 780)#linea cabecera

		#self = canvas.Canvas(filename, bottomup=0)
		f=Image('static/img/logo_Region_Cajamarca2019.png', width=147, height=50)#imagen
		#f=Image('static/img/gr2019.png', width=73, height=25)#imagen
		f.drawOn(self, 75, 780)#posicion DE LA IMAGEN en el encabezado


		self.restoreState()
	

class Listarperiodico(TemplateView):
	template_name = "listarperiodico.html"
	def pdf_Platypus(request):
		response = HttpResponse(content_type='application/pdf')#tipo de rpta
		#pdf_name = "periodicos1.pdf"  # nombre para la descarga
		#response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name #descarga con el nombre indicado
		buff = BytesIO() #almacena el doc
		#c = canvas.Canvas(buff)
		doc = SimpleDocTemplate(buff,
								pagesize=A4,
								rightMargin=50,#miderecha
								leftMargin=50,#mi izquierda
								topMargin=60,
								bottomMargin=70,#inferior hoja	                            
								)#plantilla del doc enlazado al buffer
		periodicos = []#lista para generar doc
		styles = getSampleStyleSheet()#estilos
		style = styles['Title']
		style1= styles['Normal']
		style.spaceAfter = 0.3 * inch
		style.fontSize = 21
		style.fontName = "Times-Roman"
		style.textColor = "Blue"

		#style.alignment=TA_JUSTIFY
		"""p = ParagraphStyle('parrafos', 
						   
						   fontSize = 28,
						   fontName="Times-Roman")"""
		header = Paragraph("Listado de periodicos", style)#encabezado doc
		#header = Paragraph("Listado de periodicos", styles['Heading1'])#encabezado doc
		#header = Paragraph("Listado de periodicos", p)#encabezado doc
		
		"""f=Image('static/img/admin.png', width=30, height=30)
		f.hAlign = 'LEFT'
		periodicos.append(f)
		periodicos.append(Spacer(1, 0.25*inch))"""
		periodicos.append(header)#agrega encabezado del doc a lista
		headings = ('Nombre', 'Anio', 'descripcion', 'Procede')#cabecera de tabla
	   
		allclientes = [(Paragraph(p.nombre, style1), p.anio, Paragraph(p.descripcion, style1), Paragraph(str(p.procedencia),styles['Normal'])) for p in Foto.objects.all()]#registros
		t = Table([headings] + allclientes,colWidths=(50*mm, 10*mm, 70*mm, 30*mm),repeatRows=1)#crea tabla
		#t = Table([headings] + allclientes,repeatRows=1)#crea tabla
		t.setStyle(TableStyle(
			[
			('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
			('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
			('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
			]
			))#estilos tabla
		periodicos.append(t) #agrega tabla a lista

		#doc.build(periodicos) #genera doc en base a lista
		doc.multiBuild(periodicos, canvasmaker=FooterCanvas)
		response.write(buff.getvalue()) #imprimimos el doc que sta en el buffer(pdf)
		buff.close()#cerramos buffer
		return response #retornamos pdf

	def get_context_data(self, **kwargs):
		#context = super(Home, self).get_context_data(**kwargs)
		context = super().get_context_data(**kwargs)
		context['objetos'] = Periodico.objects.all()#pasamos las periodicos
		
		return context




class Crearperiodico(CreateView):
	form_class= PeriodicoForm
	#template_name="periodicos/formularioperiodico.html"
	template_name="periodicos/formularioperiodico.html"
	model = Periodico
	#fields = '__all__'

class Actualizaperiodico(UpdateView):
	form_class= PeriodicoForm
	#template_name="periodicos/formularioactualizaperiodico.html"
	template_name="periodicos/formularioperiodico.html"
	model = Periodico
	#fields = '__all__'
class Eliminaperiodico(DeleteView):
	form_class= PeriodicoForm
	template_name="periodicos/formularioeliminaperiodico.html"
	model = Periodico
	success_url = reverse_lazy("lista_periodico")

class Eliminaorigen(DeleteView):
	form_class= OrigenForm
	template_name="periodicos/formularioeliminaorigen.html"
	model = Origen
	success_url = reverse_lazy("lista_origen")

class Listarejemplar(TemplateView):
	template_name = "listarejemplar.html"
	def pdf_Platypus(request):
		response = HttpResponse(content_type='application/pdf')#tipo de rpta
		#pdf_name = "periodicos1.pdf"  # nombre para la descarga
		#response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name #descarga con el nombre indicado
		buff = BytesIO() #almacena el doc
		#c = canvas.Canvas(buff)
		doc = SimpleDocTemplate(buff,
								pagesize=A4,
								rightMargin=50,#miderecha
								leftMargin=50,#mi izquierda
								topMargin=60,
								bottomMargin=70,#inferior hoja                              
								)#plantilla del doc enlazado al buffer
		periodicos = []#lista para generar doc
		styles = getSampleStyleSheet()#estilos
		style = styles['Title']
		style1= styles['Normal']
		style.spaceAfter = 0.3 * inch
		style.fontSize = 21
		style.fontName = "Times-Roman"
		style.textColor = "Blue"

		#style.alignment=TA_JUSTIFY
		"""p = ParagraphStyle('parrafos', 
						   
						   fontSize = 28,
						   fontName="Times-Roman")"""
		header = Paragraph("Listado de periodicos", style)#encabezado doc
		#header = Paragraph("Listado de periodicos", styles['Heading1'])#encabezado doc
		#header = Paragraph("Listado de periodicos", p)#encabezado doc
		
		"""f=Image('static/img/admin.png', width=30, height=30)
		f.hAlign = 'LEFT'
		periodicos.append(f)
		periodicos.append(Spacer(1, 0.25*inch))"""
		periodicos.append(header)#agrega encabezado del doc a lista
		headings = ('Nombre', 'Anio', 'descripcion', 'Procede')#cabecera de tabla
	   
		allclientes = [(Paragraph(p.nombre, style1), p.anio, Paragraph(p.descripcion, style1), Paragraph(str(p.procedencia),styles['Normal'])) for p in Foto.objects.all()]#registros
		t = Table([headings] + allclientes,colWidths=(50*mm, 10*mm, 70*mm, 30*mm),repeatRows=1)#crea tabla
		#t = Table([headings] + allclientes,repeatRows=1)#crea tabla
		t.setStyle(TableStyle(
			[
			('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
			('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
			('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
			]
			))#estilos tabla
		periodicos.append(t) #agrega tabla a lista

		#doc.build(periodicos) #genera doc en base a lista
		doc.multiBuild(periodicos, canvasmaker=FooterCanvas)
		response.write(buff.getvalue()) #imprimimos el doc que sta en el buffer(pdf)
		buff.close()#cerramos buffer
		return response #retornamos pdf

	def get_context_data(self, **kwargs):
		#context = super(Home, self).get_context_data(**kwargs)
		context = super().get_context_data(**kwargs)
		context['objetos'] = Ejemplar.objects.all()#pasamos las periodicos
		return context

class Crearejemplar(CreateView):
	form_class= EjemplarForm
	template_name="periodicos/formularioejemplar.html"
	model = Ejemplar
	#fields = '__all__'

class Actualizaejemplar(UpdateView):
	form_class= EjemplarForm
	template_name="periodicos/formularioejemplar.html"
	model = Ejemplar
	#fields = '__all__'
class Eliminaejemplar(DeleteView):
	form_class= EjemplarForm
	template_name="periodicos/formularioeliminaejemplar.html"
	model = Ejemplar
	success_url = reverse_lazy("lista_ejemplar")
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		if os.path.exists(str(self.object.ruta)) and os.path.isfile(str(self.object.ruta)):
			os.remove(str(self.object.ruta))
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)


	def delete(self, request, *args, **kwargs):
		"""Call the delete() method on the fetched object and then redirect to thesuccess URL."""
		self.object = self.get_object()
		success_url = self.get_success_url()
		#os.remove(self.object.objects.ruta)
		self.object.delete()
		return HttpResponseRedirect(success_url)

class Reporteejemplarperiodico(ListView):
	template_name="reporte_ejemplarperiodico.html"
	model = Ejemplar


class ReporteejemplarperiodicoPdf(Pdf):
	template_name="fotos_tipo.html"
	model = Ejemplar
	modelcampo="periodico"
	maestro = Periodico
	maestrocampo="nombre" 
	lista_cabeceras=['Fecha', 'Descripción', 'Siglo']
	lista_campos=['fecha', 'descripcion', 'siglo']
	
	#lista_datos=["valor1","valor2","valor3","valor4"]
	anchocol=(50*mm, 85*mm, 30*mm)# normal:165mm max:195
	titulo="Listado de Ejemplares del Periódico: "

def listartipos(request):
	#filtro=request.GET['tipo']
	data = Periodico.objects.all()
	libros=[tiposerializado(libro) for libro in data]
	return HttpResponse(json.dumps(libros), content_type='application/json')
	


def listarfiltros(request):
	#filtro=request.GET['tipo']
	filtro=request.POST['tipo']
	#data=Foto.objects.all()
	#data=Foto.objects.filter(id=3)
	#tipofoto = Tipofoto.objects.first()
	periodico = Periodico.objects.get(nombre=filtro)
	data=periodico.ejemplar_set.all()
	#data=Foto.objects.get(nombre__exact='Santa Teresita')
	libros=[libroserializado(libro) for libro in data]
	#data="hi"
	#data1 = serializers.serialize("json", data, fields=(nombre))
	#data =filtro
	#data = {'nombre': 'Eduardo', 'dni':'40703678', 'tel':'976649322' }
	#return HttpResponse(json.dumps(data))
	return HttpResponse(json.dumps(libros, cls=DjangoJSONEncoder), content_type='application/json')

	#return HttpResponse(data1, content_type='application/json')
	#return HttpResponse(json.dumps({'valido': False}), content_type='application/javascript')
	#return JsonResponse(json.dumps(fotos), safe=False)

def libroserializado(libro):
	return {'fecha': libro.fecha, 'id': libro.id, 'descripcion': libro.descripcion, 'siglo':libro.siglo}

def tiposerializado(libro):
	return {'nombre': libro.nombre}

