# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from polls.models import Usuario, Alarma, Timbre

class UsuarioList(ListView):
    model = Usuario
    template_name="polls/usuario_list.html"

class AlarmaList(ListView):
    model = Alarma
    template_name="polls/alarma_list.html"

class TimbreList(ListView):
    model = Timbre
    template_name="polls/timbre_list.html"