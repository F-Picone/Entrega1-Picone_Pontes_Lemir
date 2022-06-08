from django.contrib import admin
from SaludApp.models import medico,paciente,sede,paciente_nuevo

admin.site.register(medico)
admin.site.register(paciente)
admin.site.register(sede)
admin.site.register(paciente_nuevo)
