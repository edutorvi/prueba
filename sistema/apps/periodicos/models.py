from django.db import models
from django.urls import reverse,reverse_lazy
# Create your models here.
import os
from django.core.validators import MaxLengthValidator

class Origen(models.Model):
    provincia = models.CharField(max_length=32, unique=True)
    

    def __str__(self):
        return self.provincia

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('lista_origen')
        #return reverse_lazy('lista_origen')
        


class Periodico(models.Model):
   
    origen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, unique=True)
    anio_inicio = models.IntegerField()
    anio_fin = models.IntegerField()
    cantidad = models.IntegerField()
   
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('lista_periodico')
        #return reverse_lazy('lista_origen')

class Ejemplar(models.Model):
    periodico = models.ForeignKey(Periodico, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField(max_length=255, 
                                   validators=[MaxLengthValidator(255)])
    ruta = models.ImageField(upload_to='static/images/periodico')
    siglo = models.CharField(max_length=5)

    def __str__(self):
        return self.descripcion

    def campo (self,valor):
        if valor=="periodico":
            rpta=self.periodico
        elif valor=="fecha":
            rpta=self.fecha
        elif valor=="descripcion":
            rpta=self.descripcion
        elif valor=="ruta":
            rpta=self.ruta
        elif valor=="siglo":
            rpta=self.siglo

        return rpta

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('lista_ejemplar')

    def save(self, *args, **kwargs):
    
        #bd = Foto.objects.get(id=self.id)
        try:
            bd = Ejemplar.objects.get(id=self.id)
        except Ejemplar.DoesNotExist:
            bd = None
        #self.object = self.get_object()
        if bd != None:
            if self.ruta != bd.ruta:
                if os.path.exists(str(bd.ruta)) and os.path.isfile(str(bd.ruta)):
        #if os.path.exists(str(self.ruta)) and os.path.isfile(str(self.ruta)):
                    os.remove(str(bd.ruta))
        super (Ejemplar, self).save()
        #self.object.save()
        #super(MyModelName, self).save(*args, **kwargs)

