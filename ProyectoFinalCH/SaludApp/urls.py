from django.urls import path
from SaludApp.views import inicio,medicos

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('medicos/',medicos, name= 'medicos')
]