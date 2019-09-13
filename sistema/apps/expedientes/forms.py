from django import forms
from .models import Expediente,Tipoexpediente,Serie




class ExpedienteForm(forms.ModelForm):
	def clean(self):
		fecha_ext2 = self.cleaned_data['fecha_ext2']
		fecha_ext1 = self.cleaned_data['fecha_ext1']
		if fecha_ext2 <= fecha_ext1:
			raise forms.ValidationError('La fecha fecha_ext2 debe ser mayor que la fecha fecha_ext1')
		#return sección

	class Meta:
		model = Expediente
		fields = [
		'serie',
		'tipoexpediente',
		'anio',
		'legajo',
		'numero',
		'descripcion',
		'folios',
		'fecha_ext1',
		'fecha_ext2',
		'ruta',]
		labels = {
		'tipoexpediente' : 'Tipo Expediente',
		'descripcion' : 'Descripción del Expediente',
	 
		}
		
		widgets = {
		'descripcion' : forms.Textarea(attrs={ 'rows':'5'}),
	
        'fecha_ext1' : forms.TextInput(attrs={'id': 'fecha1'}),
        'fecha_ext2' : forms.TextInput(attrs={'id': 'fecha2'}),
        
		#'descripcion' : forms.Textarea(attrs={ rows:"5", 'size': 100, 'id': 'hl'}),
		#'body_text' : forms.Textarea(attrs={'class':'form-control'}),
		#'pub_date' : forms.TextInput(attrs={ 'id': 'pd'}),
		#'mod_date' : forms.DateInput(attrs={ 'id': 'md'}),
		#'n_comments' : forms.NumberInput(),
		#'n_pingbacks' : forms.NumberInput(),
		#'rating' : forms.NumberInput(),
		}
		
class TipoExpedienteForm(forms.ModelForm):

	class Meta:
		model = Tipoexpediente
		fields = [
		'nombre',
	   
		]
		labels = {
		'nombre' : 'Nombre',
	  
	 
		}

class SerieForm(forms.ModelForm):
	
	def clean_seccion (self):
		seccion = self.cleaned_data['seccion']
		if len(seccion.strip()) == 0:
			raise forms.ValidationError("Falta ingresar la sección")

		return seccion
	   
		# if Serie.objects.filter(seccion=seccion):
		# 	raise forms.ValidationError("ya existe la seccion")

		# return seccion

	def clean_nombre (self):
		datonombre = self.cleaned_data['nombre']
		
		if Serie.objects.filter(nombre=datonombre):
			raise forms.ValidationError("ya existe el nombre")

		return datonombre

	#def __init__(self):
		#super().__init__(*args, **kwargs)
		#d:dself.fields['seccion'].validators.append(titulo_validation)
	

	class Meta:
		model = Serie
		fields = [
		'seccion',
		'nombre',
	
		]
		labels = {
		'nombre' : 'Nombre',
			 
		}
