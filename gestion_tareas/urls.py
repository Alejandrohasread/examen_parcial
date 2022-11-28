from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns=[
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('detalleTarea/<str:ind>',views.detalleTarea,name='detalleTarea'),   
    path('eliminarTarea/<str:ind>', views.eliminarTarea,name='eliminarTarea')
   ]