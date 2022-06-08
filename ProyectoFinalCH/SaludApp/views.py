from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from SaludApp.models import paciente_nuevo

def inicio(self):
    plantilla = loader.get_template('SaludApp/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def medicos(request):
    return render(request, 'SaludApp/doctores.html')

def sede(request):
    return render(request, 'SaludApp/sede.html')

def especialidad(request):
    return render(request, 'SaludApp/especialidades.html')

def turnoFormulario(request):
    if request.method == "POST":
        nuevo_ingreso= paciente_nuevo(request.POST["nombre"], request.POST["apellido"],request.POST["medico_solicitado"], request.POST["sede"])
        nuevo_ingreso.save()
        return render(request, 'SaludApp/inicio.html')
    return render(request, "SaludApp/turnoFormulario.html")


