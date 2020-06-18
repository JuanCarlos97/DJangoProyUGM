"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
#from django.views.generic import TemplateView
from eleccion.casilla import CasillaListado, CasillaDetalle, CasillaCrear, CasillaActualizar, CasillaEliminar
from eleccion.candidato import CandidatoListado, CandidatoDetalle, CandidatoCrear, CandidatoActualizar, CandidatoEliminar
from eleccion.funcionario import FuncionarioListado, FuncionarioDetalle, FuncionarioCrear, FuncionarioActualizar, FuncionarioEliminar
#from . import views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Casillas
    path('casilla/', CasillaListado.as_view(template_name = "casillas/index.html"), name='casilla'), 
    path('casilla/detalle/<int:pk>', CasillaDetalle.as_view(template_name = "casillas/detalles.html"), name='detalles'), 
    path('casilla/crear', CasillaCrear.as_view(template_name = "casillas/crear.html"), name='crear'),
    path('casilla/editar/<int:pk>', CasillaActualizar.as_view(template_name = "casillas/actualizar.html"), name='actualizar'), 
    path('casilla/eliminar/<int:pk>', CasillaEliminar.as_view(), name='eliminar'),    

    # Candidatos
    path('candidato/', CandidatoListado.as_view(template_name = "candidatos/index.html"), name='candidato'), 
    path('candidato/detalle/<int:pk>', CandidatoDetalle.as_view(template_name = "candidatos/detalles.html"), name='detalles'), 
    path('candidato/crear', CandidatoCrear.as_view(template_name = "candidatos/crear.html"), name='crear'),
    path('candidato/editar/<int:pk>', CandidatoActualizar.as_view(template_name = "candidatos/actualizar.html"), name='actualizar'), 
    path('candidato/eliminar/<int:pk>', CandidatoEliminar.as_view(), name='eliminar'),  

    # Funcionarios
    path('funcionario/', FuncionarioListado.as_view(template_name = "funcionarios/index.html"), name='funcionario'), 
    path('funcionario/detalle/<int:pk>', FuncionarioDetalle.as_view(template_name = "funcionarios/detalles.html"), name='detalles'), 
    path('funcionario/crear', FuncionarioCrear.as_view(template_name = "funcionarios/crear.html"), name='crear'),
    path('funcionario/editar/<int:pk>', FuncionarioActualizar.as_view(template_name = "funcionarios/actualizar.html"), name='actualizar'), 
    path('funcionario/eliminar/<int:pk>', FuncionarioEliminar.as_view(), name='eliminar'),  
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)