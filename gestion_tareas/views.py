from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
lista_tareas =[['Lavar el baño','Limpiar el inodoro y el piso de la ducha','2022-11-25','2022-11-25','2022-11-25','Rosario'],['Pasear al perro','Sacar al perro consu correa por los alrededores y esperar a que haga sus necesidades','2022-04-06','2022-11-25','Rodrigo'],['Barrer la sala','Usar la escoba y el recogedor para limpiar la superficie del piso de la sala de tal forma que quede libre de polvo','2022-11-20','2022-11-25','ALvaro']]

def index(request):
    return HttpResponse('Esta es mi primera vista')  

#Aqui estan el usuario y la contraseña

def login(request):
    return render(request,'gestion_tareas/login.html',{
        'usuario': 'rafloresz@pucpe.edu.pe',
        'contraseña': 'levi',

    })
def dashboard(request):
    if request.method == 'POST':
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
        nuevaTarea.append(str(titulo))
        nuevaTarea.append(str(descripcion))
        nuevaTarea.append(str(fecha_creacion))
        nuevaTarea.append(str(fecha_entrega))
        nuevaTarea.append(str(usuario_designado))
        lista_tareas.append(nuevaTarea)   
     
   
    return render(request,'gestion_tareas/dashboard.html',{
        'tareas': lista_tareas,
        })

