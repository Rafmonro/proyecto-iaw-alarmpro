
from django.conf.urls import url
from django.contrib import admin
from polls.views import *


from polls.views import UsuarioList, AlarmaList, TimbreList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Usuario/', UsuarioList.as_view()),
    url(r'^Alarma/', AlarmaList.as_view()),
    url(r'^Timbre/', TimbreList.as_view()),
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', iniciarsesion, name='Login'),
    url(r'^logout',cerrarsesion,name='Logout'),
    url(r'^crearalarma',Crearalarma,name='crearalarma'),
    url(r'^Creartimbre/', CrearTimbre.as_view()),
    url(r'^Modificarusuario/(?P<pk>\d+)', ModificarUsuario.as_view()),
    url(r'^Modificartimbre/(?P<pk>\d+)', ModificarTimbre.as_view()),
    url(r'^Modificaralarma/(?P<pk>\d+)', ModificarAlarma.as_view()),
]

