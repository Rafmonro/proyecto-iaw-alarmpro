# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime 

class Usuario(models.Model):
	nombre_usuario = models.CharField(max_length=200)
	primer_apellido = models.CharField(max_length=200)
	segundo_apellido = models.CharField(max_length=200)
	alias = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.nombre_usuario)

class Alarma(models.Model):
	nombre_alarma = models.CharField(max_length=200,default='')
	longitud = models.DecimalField(max_digits=9,decimal_places=6)
	latitud = models.DecimalField(max_digits=9,decimal_places=6)
	calendario = models.DateTimeField()
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
	timbre = models.ForeignKey('Timbre',on_delete=models.CASCADE)

	def __unicode__(self):
		return unicode(self.nombre_alarma)


class Timbre(models.Model):
	file = models.FileField(upload_to='polls/timbres')
	nombre_timbre = models.CharField(max_length=200)
	

	def __unicode__(self):
		return unicode(self.nombre_timbre)
    

