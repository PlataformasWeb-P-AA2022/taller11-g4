from django.shortcuts import render

# Create your views here.
from viviendas.models import *

# importar los formularios de forms.py
from viviendas.forms import *

# Create your views here.

def index(request):

    edificio = Estudiante.objects.all()

    informacion_template = {'edificio': edificio}
    return render(request, 'index.html', informacion_template)


def obtener_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)

    informacion_template = {'edificio': edificio}
    return render(request, 'obtener_edificio.html', informacion_template)


def crear_edificio(request):
    """
    """
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)


def editar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)


def crear_numero_telefonico(request):
    """
    """

    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)


def editar_numero_telefonico(request, id):
    """
    """
    telefono = NumeroTelefonico.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST, instance=telefono)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm(instance=telefono)
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)

def crear_numero_telefonico_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoEstudianteForm(estudiante, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoEstudianteForm(estudiante)
    diccionario = {'formulario': formulario, 'estudiante': estudiante}

    return render(request, 'crearNumeroTelefonicoEstudiante.html', diccionario)
