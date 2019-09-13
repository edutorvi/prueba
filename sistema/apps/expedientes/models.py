from django.db import models
from django.urls import reverse
# Create your models here.
import os
from django.core.validators import MaxLengthValidator
from .validadores import minimo,sinespacios #archivo de validaciones
#from django.db import IntegrityError


class Tipoexpediente(models.Model):
	nombre = models.CharField(max_length=32, unique=True)
   

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
		return reverse('lista_tipo_expediente')


class Serie(models.Model):
	seccion = models.CharField(max_length=32, validators=[minimo])
	nombre = models.CharField(max_length=32, unique=True)
	def __str__(self):
		return self.nombre
	def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
		return reverse('lista_serie')


class Expediente(models.Model):
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
	tipoexpediente = models.ForeignKey(Tipoexpediente, on_delete=models.CASCADE)
	anio = models.IntegerField()
	legajo = models.CharField(max_length=5)
	numero = models.CharField(max_length=9)
	#descripcion = models.CharField(max_length=255)
	#descripcion = models.TextField()
	descripcion = models.TextField(max_length=300, blank=True,
								   validators=[MaxLengthValidator(300)])
	folios = models.IntegerField()
	fecha_ext1 = models.DateField() 
	fecha_ext2 = models.DateField()
	ruta = models.ImageField(upload_to='static/images/expedientes', null=True, blank=True)

	def __str__(self):
		return self.descripcion

	def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
		return reverse('lista_expediente')

	def save(self, *args, **kwargs):
	
		#bd = Foto.objects.get(id=self.id)
		try:
			bd = Expediente.objects.get(id=self.id)
		except Expediente.DoesNotExist:
			bd = None
		#self.object = self.get_object()
		if bd != None:
			if self.ruta != bd.ruta:
				if os.path.exists(str(bd.ruta)) and os.path.isfile(str(bd.ruta)):
		#if os.path.exists(str(self.ruta)) and os.path.isfile(str(self.ruta)):
					os.remove(str(bd.ruta))
		super (Expediente, self).save()
		#self.object.save()
		#super(MyModelName, self).save(*args, **kwargs)





