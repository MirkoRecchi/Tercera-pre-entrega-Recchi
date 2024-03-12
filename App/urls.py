
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', Inicio, name="inicio"),
    path('participante/', participante , name="participante"),
    path('jurado/', jurado , name="jurado"),
    path('libro/', libro , name="libro"),
    path('calificacion/', calificacion , name="calificacion"),
    #------------------Formulario urls-----------------------
    path('participante_form/', participanteForm , name="participante_form"),
    path('libro_form/', libroForm , name="libro_form"),
    path('calificacion_form/', calificacionForm , name="calificacion_form"),
    #------------------Busqueda urls--------------------------------------
    path('buscar_calificacion/', BuscarCalificacion , name="buscar_calificacion"),
    path('encontrar_calificacion/', EncontrarCalificacion , name="encontrar_calificacion"),
]


