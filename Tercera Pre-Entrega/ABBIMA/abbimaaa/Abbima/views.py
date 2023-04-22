from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from .forms import ProfesorForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.urls import reverse_lazy

# Create your views here.

def crear_curso(request):

    nombre_curso="Program"
    comision_curso=10010
    print("Creando")
    curso=Curso(comision=comision_curso,  nombre=nombre_curso, )
    curso.save()
    respuesta=f"Curso creado--- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

    
def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.apellido = form.cleaned_data['apellido']
            profesor.nombre = form.cleaned_data['nombre']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all()
    
    return render(request, "Abbima/profesores.html", {"profesores": profesores, "form" : form})


def busquedaComision(request):
    return render(request, "Abbima/busquedaComision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)
        return render(request, "Abbima/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "Abbima/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})


def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form = ProfesorForm()
    return render(request, "Abbima/Profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente", "form": form})



def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form= ProfesorForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            profesor.nombre=info["nombre"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.apellido=info["apellido"]
            
            profesores=Profesor.objects.all()
            profesor.save()
            
            form = ProfesorForm()
            return render(request, "Abbima/Profesores.html" ,{"profesores":profesores, "mensaje": "Profesor editado ", "form": form})
        pass
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido,  "profesion":profesor.profesion "email":profesor.email,})
        return render(request, "Abbima/editarProfesor.html", {"form": formulario, "profesor": profesor})

def estudiantes(request):
    return render(request, "Abbima/estudiantes.html")

def entregables(request):
    return render(request, "Abbima/entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido ")

def inicioApp(request):
    return render(request, "Abbima/inicio.html")



class EstudianteList(ListView):
    model= Estudiante
    template_name= "Abbima/estudiantes.html"

class EstudianteDetalle(DetailView): 
    model=Estudiante
    template_name="estudiantes.html"

class EstudianteCreacion(CreateView):
    model= Estudiante
    success_url= reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']


class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields=['nombre', 'apellido', 'email']


    

