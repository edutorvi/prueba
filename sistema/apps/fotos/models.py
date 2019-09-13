from django.db import models
from django.urls import reverse
# Create your models here.
import os
from django.core.validators import MaxLengthValidator

class Tipofoto(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    serie = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('lista_tipo_foto')

    def fitro(self,campo):

        return Tipofoto.objects.get(nombre=filtro)


class Procedencia(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
   
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('lista_procedencia')


class Foto(models.Model):
    tipofoto = models.ForeignKey(Tipofoto, on_delete=models.CASCADE)
    procedencia = models.ForeignKey(Procedencia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, unique=True)
    #descripcion = models.CharField(max_length=255)
    #descripcion = models.TextField()
    descripcion = models.TextField(max_length=255, blank=True,
                                   validators=[MaxLengthValidator(255)])
    anio = models.IntegerField()
    obs = models.CharField(max_length=30, null=True, blank=True)
    #ruta = models.CharField(max_length=50)
    ruta = models.ImageField(upload_to='static/images/fotos')

    def campo (self,valor):
        if valor=="nombre":
            rpta=self.nombre
        elif valor=="procedencia":
            rpta=self.procedencia
        elif valor=="descripcion":
            rpta=self.descripcion
        elif valor=="anio":
            rpta=self.anio
        elif valor=="tipofoto":
            rpta=self.tipofoto

        return rpta

    


    def __str__(self):
        return self.nombre

    def get_absolute_url(self):#redirreciona cuando se crea un nuevo registro
        return reverse('listar')

    def save(self, *args, **kwargs):
    
        #bd = Foto.objects.get(id=self.id)
        try:
            bd = Foto.objects.get(id=self.id)
        except Foto.DoesNotExist:
            bd = None
        #self.object = self.get_object()
        if bd != None:
            if self.ruta != bd.ruta:
                if os.path.exists(str(bd.ruta)) and os.path.isfile(str(bd.ruta)):
        #if os.path.exists(str(self.ruta)) and os.path.isfile(str(self.ruta)):
                    os.remove(str(bd.ruta))
        super (Foto, self).save()
        #self.object.save()
        #super(MyModelName, self).save(*args, **kwargs)


class FotoImage(models.Model):
    foto = models.ForeignKey(Foto, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/')

    def __unicode__(self,):
        return str(self.image)

