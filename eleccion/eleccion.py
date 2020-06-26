from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eleccion
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms
 
# Eleccion
class EleccionListado(ListView): 
    model = Eleccion
 
class EleccionDetalle(DetailView): 
    model = Eleccion
 
class EleccionCrear(SuccessMessageMixin, CreateView): 
    model = Eleccion
    form = Eleccion
    fields = "__all__" 
    success_message = 'Eleccion Creada Correctamente !' # Mostramos este Mensaje luego de Crear     
 
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):        
        return reverse('eleccion') # Redireccionamos a la vista principal 'leer' 
 
class EleccionActualizar(SuccessMessageMixin, UpdateView): 
    model = Eleccion
    form = Eleccion
    fields = "__all__"  
    success_message = 'Eleccion Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar 
 
    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):               
        return reverse('eleccion') # Redireccionamos a la vista principal 'leer' 
 
class EleccionEliminar(SuccessMessageMixin, DeleteView): 
    model = Eleccion 
    form = Eleccion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self): 
        success_message = 'Eleccion Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un 
        messages.success (self.request, (success_message))       
        return reverse('eleccion') # Redireccionamos a la vista principal 'leer'