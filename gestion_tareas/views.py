from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')  

#Aqui estan el usuario y la contraseña

def login(request):
    return render(request,'gestion_tareas/login.html',{
        'usuario': 'rafloresz@pucpe.edu.pe',
        'contraseña': 'levi',

    })
def dashboard(request):
    return render(request,'gestion_tareas/dashboard.html',)

