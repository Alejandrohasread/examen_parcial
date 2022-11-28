from django.shortcuts import render
from .models import usuario, tarea
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
 

#Aqui estan el usuario y la contraseña

def login(request):
    usuariosInformacion = usuario.objects.all().order_by('id')
    return render(request,'gestion_tareas/login.html',{
        'usuarios': usuariosInformacion[0] ,
        })
def dashboard(request):
    tareasInformacion = tarea.objects.all().order_by('id')
    usuariosInformacion = usuario.objects.all().order_by('id')
    usuario0= usuariosInformacion[0].nombres + ' ' + usuariosInformacion[0].apellidos
    usuario1= usuariosInformacion[1].nombres + ' ' + usuariosInformacion[1].apellidos
    usuario2= usuariosInformacion[2].nombres + ' ' + usuariosInformacion[2].apellidos
    usuario3= usuariosInformacion[3].nombres + ' ' + usuariosInformacion[3].apellidos
    usuario4= usuariosInformacion[4].nombres + ' ' + usuariosInformacion[4].apellidos

    if request.method == 'POST':
        if 'Crear' in request.POST:
            nuevaTarea = []
            print('Hola, se ha posteado la información ')
            titulo = request.POST.get('tituloTarea')
            descripcion = request.POST.get('descripcionTarea')
            fecha_creacion = request.POST.get('creacionTarea')
            fecha_entrega = request.POST.get('entregaTarea')
            usuario_designado = request.POST.get('designadoTarea')
            print('El título de la tarea es: ' + str(titulo))
            print('La descripción de la tarea es: ' + str(descripcion))
            print('La fecha de creación de la tarea es: ' + str(fecha_creacion))
            print('La fecha de entrega de la tarea es: ' + str(fecha_entrega))
            print('El usuario designado de la tarea es: ' + str(usuario_designado))    
            tarea(titulo = str(titulo),descripcion = str(descripcion),fecha_creacion = str(fecha_creacion),fecha_entrega = str(fecha_entrega),usuario_designado = str(usuario_designado)).save()
            tareasInformacion = tarea.objects.all().order_by('id')    
        elif 'Filtrar' in request.POST:
                filtradoDesignado = request.POST.get('designadoFiltrado')    
                tareasInformacion = tarea.objects.filter(usuario_designado=filtradoDesignado)
    return render(request,'gestion_tareas/dashboard.html',{
        'tareasInformacion': tareasInformacion,
        'usuario0': usuario0,
        'usuario1': usuario1,
        'usuario2': usuario2,
        'usuario3': usuario3,
        'usuario4': usuario4 ,
        })

def detalleTarea(request,ind):
        tarea_seleccionada = tarea.objects.get(id=ind)
        return render(request,'gestion_tareas/detalleTarea.html',{
            'tarea_seleccionada': tarea_seleccionada
        })

def eliminarTarea(request,ind):
    tarea_eliminar = tarea.objects.get(id=ind)
    tarea_eliminar.delete()
    return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))       

  