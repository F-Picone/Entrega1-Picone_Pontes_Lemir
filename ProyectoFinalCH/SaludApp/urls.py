from django.urls import path
from SaludApp.views import inicio

urlpatterns = [
    path('', inicio, name= 'inicio'),
]