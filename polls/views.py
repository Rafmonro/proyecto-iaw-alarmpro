# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from polls.models import Usuario, Alarma, Timbre
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import Http404,HttpResponseRedirect,HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from polls.forms import *


class UsuarioList(ListView):
    model = Usuario
    template_name="polls/usuario_list.html"

class AlarmaList(ListView):
    model = Alarma
    template_name="polls/alarma_list.html"

class TimbreList(ListView):
    model = Timbre
    template_name="polls/timbre_list.html"

class CrearTimbre(CreateView):
    model = Timbre
    fields = '__all__'
    template_name="polls/creartimbre.html"
    success_url = '/Timbre'

class ModificarUsuario(UpdateView):
    model = Usuario
    fields = '__all__'
    template_name = 'polls/modificarusuario.html'
    success_url = '/Usuario'

class ModificarTimbre(UpdateView):
    model = Timbre
    fields = '__all__'
    template_name = 'polls/modificartimbre.html'
    success_url = '/Timbre'

class ModificarAlarma(UpdateView):
    model = Alarma
    fields = '__all__'
    template_name = 'polls/modificaralarma.html'
    success_url = '/Alarma'

#class AuthorDelete(DeleteView):
#    model = Author
#    success_url = reverse_lazy('author-list')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/admin')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})

def iniciarsesion(request):
	if request.method == 'POST':
		form = IniciarSesion(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("No se ha podido iniciar sesión")
	else:
		form = IniciarSesion()
	return render(request,'polls/login.html',{'form':form})

def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect('login')

def Crearalarma(request):
	if request.method == 'POST':
		form = CrearAlarma(request.POST,request.FILES)
		if form.is_valid():
			alarma = Alarma()
			usuario = Usuario.objects.get(user=request.user)
			alarma.nombre_alarma = form.cleaned_data.get('nombre_alarma')
			alarma.longitud = form.cleaned_data.get('longitud')
			alarma.latitud = form.cleaned_data.get('latitud')
			alarma.calendario = form.cleaned_data.get('calendario')
			alarma.usuario = usuario
			alarma.timbre = form.cleaned_data.get('timbre')
			alarma.save()
			return HttpResponseRedirect('Alarma')
	else:
		form = CrearAlarma()
		
	return render(request,'polls/Crearalarma.html',{'form':form})