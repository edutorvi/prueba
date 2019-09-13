
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
    
        ]
        labels = {
        'username' : 'Nombre para usuario',
        'first_name' : 'Nombre',
        'last_name' : 'Apellido',
        'email' : 'Correo',
       
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
