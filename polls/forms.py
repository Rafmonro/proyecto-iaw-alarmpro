from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from polls.models import *

class SignUpForm(UserCreationForm):
	alias = forms.CharField(max_length=200)

   	class Meta:
   		model = User
   		fields = ('username','alias','first_name','last_name','email','password1','password2')


class IniciarSesion(forms.Form):
	username = forms.CharField(max_length=500)
	password = forms.CharField(max_length=500)


class CrearAlarma(forms.Form):
	nombre_alarma = forms.CharField(max_length=200)
	longitud = forms.DecimalField(max_digits=9,decimal_places=6)
	latitud = forms.DecimalField(max_digits=9,decimal_places=6)
	calendario = forms.DateTimeField()
	timbre =forms.ModelChoiceField(queryset=Timbre.objects.all())
