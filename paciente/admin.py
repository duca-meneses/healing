from django.contrib import admin

from paciente.models import Consulta, Documento

admin.site.register(Consulta)
admin.site.register(Documento)
