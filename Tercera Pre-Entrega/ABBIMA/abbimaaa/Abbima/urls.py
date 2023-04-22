from django.urls import path
from .views import *


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    path("crear_curso/", crear_curso),
    path("cursos/", cursos, name="cursos"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("buscar/", buscar, name="buscar"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),
    path("estudiante/list/", EstudianteList.as_view(), name="estudiante_list"),
    
    
    
]
