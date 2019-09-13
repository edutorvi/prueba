from django.views.generic import TemplateView

from io import BytesIO#PARA REPORTLAB

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

from django.http import HttpResponse

from apps.fotos.models import Foto,Tipofoto

class Pdf(TemplateView):
	template_name="fotos_tipo.html"
	model = Foto
	modelcampo="tipofoto"
	maestro = Tipofoto
	maestrocampo="nombre" 
	lista_cabeceras=['Nombre5', 'Año', 'Descripción', 'Procede']
	lista_campos=['nombre', 'anio', 'descripcion', 'procedencia']
	anchocol=(50*mm, 15*mm, 70*mm, 30*mm)
	titulo="LISTADO DE FOTOS POR "

	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/pdf')#tipo de rpta
		#pdf_name = "fotos1.pdf"  # nombre para la descarga
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
		fotos = []#lista para generar doc
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
		

		filtro = self.kwargs.get('filtro') # El mismo nombre que en tu URL<nombre>
		#pk = self.kwargs.get('pk') # El mismo nombre que en tu URL

		fotos.append(Spacer(1, 0.25*inch))#spacio antes del titulo
		header = Paragraph(self.titulo+filtro, style)#encabezado doc
		#header = Paragraph("Listado de Fotos", styles['Heading1'])#encabezado doc
		#header = Paragraph("Listado de Fotos", p)#encabezado doc
		
		"""f=Image('static/img/admin.png', width=30, height=30)
		f.hAlign = 'LEFT'
		fotos.append(f)
		fotos.append(Spacer(1, 0.25*inch))"""
		fotos.append(header)#agrega encabezado del doc a lista
		headings = self.lista_cabeceras#cabecera de tabla
		#headings = (self.campo1, self.campo2, self.campo3, self.campo4)#cabecera de tabla
		#filtro=request.GET['tipo']
		
		kwargs1 = {}
		kwargs1[self.maestrocampo] = filtro
	
		#eventos = Evento.objects.filter(**kargs) w
		objetofk = self.maestro.objects.get(**kwargs1)
		#tipofoto = self.maestro.objects.get(nombre=filtro)
		kwargs2 = {}
		kwargs2[self.modelcampo] = objetofk
		data=self.model.objects.filter(**kwargs2)
		#data=self.model.objects.filter(tipofoto=tipofoto)
		#data=tipofoto.foto_set.all()
		allclientes=[]
		fila=-1
	
		n = len(data)
		m = len(self.lista_campos)
		matriz = [[0] * m for i in range(n)]
		for p in data:
			
			fila=fila+1
				#if f.name==self.lista_campos[0]:
			
			for campos in range(len(self.lista_campos)):
				matriz[fila][campos]=[Paragraph(str(p.campo(self.lista_campos[campos])), style1)]
			
		allclientes.extend(matriz)
			#allclientes.append([lista1[0],lista1[1],lista1[2],lista1[3]])#agrega cada registro en una lista extendiendola
			#allclientes.extend([lista])
			#allclientes.extend([(Paragraph(p.nombre, style1), p.anio, Paragraph(p.descripcion, style1), Paragraph(str(p.procedencia),styles['Normal']))])

		#allclientes = [(Paragraph(p.nombre, style1), p.anio, Paragraph(p.descripcion, style1), Paragraph(str(p.procedencia),styles['Normal'])) for p in data]#registros
		t = Table([headings] + allclientes,colWidths=self.anchocol,repeatRows=1)#crea tabla
		#t = Table([headings] + allclientes,repeatRows=1)#crea tabla
		t.setStyle(TableStyle(
			[
			('GRID', (0, 0), (4, -1), 1, colors.Color(red=(33.0/255),green=(147.0/255),blue=(243.0/255))),
			('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
			('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(33.0/255),green=(147.0/255),blue=(243.0/255)))
			]
			))#estilos tabla
		fotos.append(t) #agrega tabla a lista

		#doc.build(fotos) #genera doc en base a lista
		doc.title = self.titulo+filtro # si no se coloca aparece anonymous
		doc.multiBuild(fotos, canvasmaker=FooterCanvas)

		response.write(buff.getvalue()) #imprimimos el doc que sta en el buffer(pdf)
		buff.close()#cerramos buffer
		return response #retornamos pdf
		#return render(response, self.template_name)


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
		self.setStrokeColorRGB(0, 0, 0)#color de linea
		self.setLineWidth(0.5)
		self.line(66, 71, A4[0] - 66, 71)#linea footer
		self.setFont('Times-Roman', 10)
		self.drawString(A4[0]-x1, 59, page1)#texto footer
		
		# self.setFont('Times-Roman', 12)
		# self.drawString(A4[0]-x2, 785, page2)#texto cabecera
		self.line(66, 780, A4[0] - 66, 780)#linea cabecera

		#self = canvas.Canvas(filename, bottomup=0)
		f=Image('static/img/logo.png', width=137, height=25)#imagen
		#f=Image('static/img/gr2019.png', width=73, height=25)#imagen
		f.drawOn(self, 230, 785)#posicion DE LA IMAGEN en el encabezado


		self.restoreState()
