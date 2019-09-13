from django import forms
from .models import Foto,Tipofoto,Procedencia
from .models import FotoImage


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = FotoImage
        fields = ['foto', 'image']


class FotoForm(forms.ModelForm):

    class Meta:
        model = Foto
        fields = ['tipofoto',
        'procedencia',
        'nombre',
        'descripcion',
        'anio',
        'obs',
        'ruta',]
        labels = {
        'tipofoto' : 'Tipo_Foto',
        'nombre' : 'Titulo de la foto',
     
        }
        
        widgets = {
        'descripcion' : forms.Textarea(attrs={ 'rows':'5'}),
        #'descripcion' : forms.Textarea(attrs={ rows:"5", 'size': 100, 'id': 'hl'}),
        #'body_text' : forms.Textarea(attrs={'class':'form-control'}),
        #'pub_date' : forms.TextInput(attrs={ 'id': 'pd'}),
        #'mod_date' : forms.DateInput(attrs={ 'id': 'md'}),
        #'n_comments' : forms.NumberInput(),
        #'n_pingbacks' : forms.NumberInput(),
        #'rating' : forms.NumberInput(),
        }
        
class TipoFotoForm(forms.ModelForm):

    class Meta:
        model = Tipofoto
        fields = [
        'nombre',
        'serie',
        ]
        labels = {
        'nombre' : 'Nombre',
        'serie' : 'Serie',
     
        }

class ProcedenciaForm(forms.ModelForm):

    class Meta:
        model = Procedencia
        fields = [
        'nombre',
    
        ]
        labels = {
        'nombre' : 'Nombre',
             
        }
