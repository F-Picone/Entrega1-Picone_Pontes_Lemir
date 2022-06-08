from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from SaludApp.models import paciente_nuevo,paciente,medico
from SaludApp.forms import paciente_formulario

def inicio(self):
    plantilla = loader.get_template('SaludApp/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def sede(request):
    return render(request, 'SaludApp/sede.html')

def especialidad(request):
    return render(request, 'SaludApp/especialidades.html')

def turnoFormulario(request):
    if request.method == "POST":
        miFormulario = paciente_formulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre= informacion["nombre"]
        apellido= informacion["apellido"]
        medico_solicitado= informacion["medico_solicitado"]
        sede= informacion["sede"]
        nuevo_ingreso= paciente_nuevo(nombre=nombre, apellido= apellido, medico_solicitado=medico_solicitado, sede=sede)
        nuevo_ingreso.save()
        return render(request, 'SaludApp/inicio.html')
    else:
        miFormulario = paciente_formulario()
    return render(request, "SaludApp/turnoFormulario.html", {'miFormulario':miFormulario})

def busquedaMedico(request):
    return render(request, 'SaludApp/doctores.html')

def buscar(request):
    if request.GET['apellido']:
        apellido= request.GET['apellido']
        apellidos= medico.objects.filter(apellido=apellido)
        apellidos= medico.objects.all()
        return render(request, 'SaludApp/resultadosBusqueda.html', {'apellido':apellido})
    else:
        respuesta= f"No se ha ingresado un medico"
        return HttpResponse(respuesta)


