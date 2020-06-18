from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Casilla, Candidato
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms
 
# Ccasillas
class CasillaListado(ListView): 
    model = Casilla
 
class CasillaDetalle(DetailView): 
    model = Casilla
 
class CasillaCrear(SuccessMessageMixin, CreateView): 
    model = Casilla
    form = Casilla
    fields = "__all__" 
    success_message = 'Casilla Creada Correctamente !' # Mostramos este Mensaje luego de Crear     
 
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):        
        return reverse('casilla') # Redireccionamos a la vista principal 'leer' 
 
class CasillaActualizar(SuccessMessageMixin, UpdateView): 
    model = Casilla
    form = Casilla
    fields = "__all__"  
    success_message = 'Casilla Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar 
 
    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):               
        return reverse('casilla') # Redireccionamos a la vista principal 'leer' 
 
class CasillaEliminar(SuccessMessageMixin, DeleteView): 
    model = Casilla 
    form = Casilla
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self): 
        success_message = 'Casilla Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un 
        messages.success (self.request, (success_message))       
        return reverse('casilla') # Redireccionamos a la vista principal 'leer'