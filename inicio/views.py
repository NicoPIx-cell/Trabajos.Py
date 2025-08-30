from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Computadora
from inicio.forms import FormularioCrearComputadora, FormularioBuscarComputadora
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def crear_computadora(request):
    print(request.POST)
    print("FILES:", request.FILES)
    
    if request.method == "POST":
        formulario = FormularioCrearComputadora(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            computadora = Computadora(marca=info.get('marca'), modelo=info.get('modelo'), imagen=info.get("imagen"), precio=info.get("precio"))
            computadora.save()
            
            return redirect("listado_de_computadora")
    else:
        formulario = FormularioCrearComputadora()
    
    return render(request, 'crear_computadora_v2.html', {'formulario': formulario})

def listado_de_computadora(request):
    
    formulario = FormularioBuscarComputadora(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data['marca']
        modelo_a_buscar = formulario.cleaned_data['modelo']
        computadora_buscadas = Computadora.objects.filter(marca__icontains=marca_a_buscar, modelo__icontains=modelo_a_buscar)
    
    return render(request, 'listado_de_computadora.html', {'computadora_buscadas': computadora_buscadas, 'formulario': formulario})


def computadora_detalle(request, id_computadora):
    computadora = Computadora.objects.get(id=id_computadora)
    return render(request, 'computadora_detalle.html', {'computadora': computadora})

class ComputadoraBorrar(LoginRequiredMixin, DeleteView):
    model = Computadora
    template_name = "computadora_borrar.html"
    success_url = reverse_lazy("listado_de_computadora")


class ComputadoraActualizar(LoginRequiredMixin, UpdateView):
    model = Computadora
    template_name = "computadora_actualizar.html"
    success_url = reverse_lazy("listado_de_computadora")
    fields = "__all__"


def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")

@login_required
def editar_precio(request, id_computadora):
    computadora = Computadora.objects.get(id=id_computadora)
    
    if request.method == 'POST':
        nuevo_precio = request.POST.get('precio')
        if nuevo_precio:
            computadora.precio = int(nuevo_precio)
            computadora.save()
            return redirect('listado_de_computadora')
    
    return render(request, 'editar_precio.html', {'computadora': computadora})