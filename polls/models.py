# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombre_usuario = models.CharField(max_length=200)
	primer_apellido = models.CharField(max_length=200)
	segundo_apellido = models.CharField(max_length=200)
	alias = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.user.username)


@receiver(post_save, sender=User)
def update_user_usuario(sender, instance, created, **kwargs):
	if created:
		Usuario.objects.create(user=instance)
	instance.usuario.save()



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
    

