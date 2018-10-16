
from django.conf.urls import url
from django.contrib import admin


from polls.views import UsuarioList, AlarmaList, TimbreList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Usuario/', UsuarioList.as_view()),
    url(r'^Alarma/', AlarmaList.as_view()),
    url(r'^Timbre/', TimbreList.as_view()),
]

