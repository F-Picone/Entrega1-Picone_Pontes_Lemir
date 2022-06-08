from django.urls import path
from SaludApp.views import inicio,medicos, sede,especialidad,turnoFormulario

urlpatterns = [
    path('', inicio , name= 'inicio'),
    path('medicos/', medicos , name= 'medicos'),
    path('sede/', sede , name='sede'),
    path('especialidad/', especialidad , name='especialidad'),
    path('turnoFormulario/', turnoFormulario , name='turnoFormulario') # FORMULARIO
]