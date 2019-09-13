# my_app/validators.py

#from django.core.exceptions import ValidationError
#forms.ValidationError, no core.exceptions.ValidationError.
from django import forms
#from django import forms.ValidationError


def minimo (value):
    if not len(value) > 4:
        #raise ValidationError('Mínimo 4 caracteres')
        raise forms.ValidationError("Aqui debe ingresar mínimo 5 caracteres")

def sinespacios(value):
	if len(value.strip()) == 0:
		raise forms.ValidationError("Falta ingresar un dato válido")