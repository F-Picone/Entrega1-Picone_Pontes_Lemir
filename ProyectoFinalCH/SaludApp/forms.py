from cgitb import html


from django import forms 

class paciente_nuevo(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    medico_solicitado = forms.CharField(max_length=40)
    sede = forms.CharField(max_length=40)
