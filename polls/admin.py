# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Usuario, Alarma, Timbre

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Timbre)
admin.site.register(Alarma)

