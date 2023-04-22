"""proyecto51325 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio/", inicio),
    path("AppCoder/", include("AppCoder.urls")),
    
    path("busquedaComision/", busquedaComision, name=busquedaComision),
    path("buscar/", buscar , name="buscar"),

    path("eliminarProfesor/<ID>", eliminarProfesor, name="estudanteList" ),
    path("editarprofesor/<ID>", editarProfesor.as_view(), name="estdiante_crear"),

    path("estudiante/list/", EstudianteList.as_view(), name="estdiante_list"),
    path("estudiante/nuevo/", EstudianteCreacion.as_view(), name="estdiante_crear"),
    path("estudiante/<PK>", EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path("estudiante/editar/<PK>", EstudianteUpdate.as_view(), name="estudiante_editar"),
    path("estudianteBorrar/<PK>", EstudianteDetalle.as_view(), name="estudiante_Borrar"),

    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", logoutView.as_view())


]