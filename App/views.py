from django.shortcuts import render
from .models import *
from .forms import *

def Inicio (request):
    return render(request , "App/index.html")


def participante (request):
    contexto = {'participante': Participante.objects.all()}
    return render(request , "App/participante.html", contexto)


def jurado (request):
    contexto = {'jurado': Jurado.objects.all()}
    return render(request , "App/jurado.html", contexto)

def libro (request):
    contexto = {'libro': Libro.objects.all()}
    return render(request , "App/libro.html", contexto)


def calificacion (request):
    contexto = {'calificacion': Calificacion.objects.all()}
    return render(request , "App/calificacion.html", contexto)


#Formularios

#---------------------------------FormularioParticipante------------------------------------------------

def participanteForm(request):
    if request.method == "POST":
        miForm = ParticipanteForm(request.POST)
        if miForm.is_valid():
            participante_nombre = miForm.cleaned_data.get("nombre")
            participante_apellido = miForm.cleaned_data.get("apellido")
            participante_edad = miForm.cleaned_data.get("edad")
            participante = Participante(nombre=participante_nombre, apellido=participante_apellido,edad=participante_edad)
            participante.save()

            contexto = {'participante': Participante.objects.all()}
            return render(request , "App/participante.html", contexto) 
    else:
        miForm = ParticipanteForm()

    return render(request, "App/participanteForm.html", {"form": miForm} )

#---------------------------------FormularioLibros------------------------------------------------
def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro_nombre = miForm.cleaned_data.get("nombre")
            libro_cantidadletras = miForm.cleaned_data.get("cantidadLetras")
            libro = Libro(nombre=libro_nombre, cantidadLetras=libro_cantidadletras)
            libro.save()

            contexto = {'libro': Libro.objects.all()}
            return render(request , "App/libro.html", contexto) 
    else:
        miForm = LibroForm()

    return render(request, "App/libroForm.html", {"form": miForm} )

#---------------------------------FormularioCalificacion------------------------------------------------
def calificacionForm(request):
    if request.method == "POST":
        miForm = CalificacionForm(request.POST)
        if miForm.is_valid():
            calificacion_nota = miForm.cleaned_data.get("nota")
            calificacion_nombreJurado = miForm.cleaned_data.get("nombreJurado")
            calificacion_nombreLibro = miForm.cleaned_data.get("nombreLibro")
            calificacion = Calificacion(nota=calificacion_nota, nombreJurado=calificacion_nombreJurado,nombreLibro=calificacion_nombreLibro)
            calificacion.save()

            contexto = {'calificacion': Calificacion.objects.all()}
            return render(request , "App/calificacion.html", contexto) 
    else:
        miForm = CalificacionForm()

    return render(request, "App/calificacionForm.html", {"form": miForm} )

#Busqueda
#Esta busqueda la realiza el participante cuando desea saber la nota de su libro
def BuscarCalificacion(request):
    return render(request, "App/buscar.html")

def EncontrarCalificacion(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        calificacion = Calificacion.objects.filter(nombreLibro__icontains=patron)
        contexto = {"calificacion": calificacion}
        return render(request, "App/calificacion.html", contexto)
    

    contexto = {'calificacion': Calificacion.objects.all()}
    return render(request , "App/calificacion.html", contexto) 
