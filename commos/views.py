from django.shortcuts import render, redirect
from .models import Notas
from django.db import IntegrityError

# Create your views here.


def index(request):
    notas= Notas.objects.all()
    return render(request,"index.html",{"notas":notas})

def registrar(request):
    return render(request,"NuevaNota.html")

def registrarNota(request):
    mensaje_error = None

    if request.method == 'POST':
        codigo = request.POST['codigo']
        nota = request.POST['nota']
        fecha = request.POST['fecha']

        # Verifica si ya existe un registro con el mismo código
        existe_registro = Notas.objects.filter(codigo=codigo).exists()

        if not existe_registro:
            # Si no existe, crea el nuevo registro
            notas = Notas.objects.create(codigo=codigo, nota=nota, fecha=fecha)
            return redirect('/')
        else:
            # Si ya existe un registro con el mismo código, muestra un mensaje de error
            mensaje_error = f"Ya existe un registro con el código {codigo}. Intente con otro código."

    # Renderiza la plantilla con el mensaje de error
    return render(request, 'NuevaNota.html', {'mensaje_error': mensaje_error})

def ver(request,codigo):
    nota=Notas.objects.get(codigo=codigo)
    return render(request,"ver.html",{"nota":nota})
    
def edicion(request,codigo):
    nota=Notas.objects.get(codigo=codigo)
    return render(request,"edicion.html",{"nota":nota})

def borrar(request,codigo):

    nota=Notas.objects.get(codigo=codigo)
    nota.delete()
    return redirect('/')

def editarNota(request):
    codigo=request.POST['codigo']
    notas=request.POST['nota']
    fecha=request.POST['fecha']

    nota=Notas.objects.get(codigo=codigo)
    nota.nota=notas
    nota.fehca=fecha
    nota.save()

    
    return redirect('/')
