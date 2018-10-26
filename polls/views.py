# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from polls.models import Usuario, Alarma, Timbre

from django.contrib.auth import login, authenticate
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
