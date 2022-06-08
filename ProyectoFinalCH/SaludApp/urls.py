from django.urls import path
from SaludApp.views import inicio, sede,especialidad,turnoFormulario,busquedaMedico

urlpatterns = [
    path('', inicio , name= 'inicio'),
    path('medicos/', busquedaMedico , name= 'medicos'), # BUSCAR MEDICOS QUE TRABAJEN AHI
    path('sede/', sede , name='sede'),
    path('especialidad/', especialidad , name='especialidad'),
    path('turnoFormulario/', turnoFormulario , name='turnoFormulario'), # FORMULARIO

]