from django import forms
from .models import Periodico,Origen,Ejemplar


class PeriodicoForm(forms.ModelForm):

    class Meta:
        model = Periodico
        fields = [
        'origen',
        'nombre',
        'anio_inicio',
        'anio_fin',
        'cantidad',
        ]
        labels = {
        'origen' : 'Origen_Periódico',
        
     
        }
        """
        widgets = {
        'headline' : forms.TextInput(attrs={'size': 100, 'id': 'hl'}),
        'body_text' : forms.Textarea(attrs={'class':'form-control'}),
        'pub_date' : forms.TextInput(attrs={ 'id': 'pd'}),
        'mod_date' : forms.DateInput(attrs={ 'id': 'md'}),
        'n_comments' : forms.NumberInput(),
        'n_pingbacks' : forms.NumberInput(),
        'rating' : forms.NumberInput(),
        }
        """
class OrigenForm(forms.ModelForm):

    class Meta:
        model = Origen
        fields = [
        'provincia',
        
        ]
        labels = {
        'provincia' : 'Provincia',
       
     
        }

class EjemplarForm(forms.ModelForm):

    def clean(self):
        perio = self.cleaned_data['periodico']
        fechaperio = self.cleaned_data['fecha']
        if Ejemplar.objects.filter(periodico=perio, fecha=fechaperio):
            #raise forms.ValidationError("ya existe un ejemplar de esta fecha")
            self.add_error('fecha', "Ya existe un ejemplar de esta fecha para dicho periódico" )

    class Meta:
        model = Ejemplar
        fields = [
        'periodico',
        'fecha',
        'descripcion',
        'ruta',
        'siglo',
        ]
        labels = {
        'fecha' : 'Publicado',
        
     
        }
        widgets = {
        'fecha' : forms.TextInput(attrs={'id': 'fecha'}),
        
        }