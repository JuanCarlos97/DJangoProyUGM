from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Funcionario
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms
 
# Ccasillas
class FuncionarioListado(ListView): 
    model = Funcionario
 
class FuncionarioDetalle(DetailView): 
    model = Funcionario
 
class FuncionarioCrear(SuccessMessageMixin, CreateView): 
    model = Funcionario
    form = Funcionario
    fields = "__all__" 
    success_message = 'Funcionario Creado Correctamente !' # Mostramos este Mensaje luego de Crear     
 
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):        
        return reverse('funcionario') # Redireccionamos a la vista principal 'leer' 
 
class FuncionarioActualizar(SuccessMessageMixin, UpdateView): 
    model = Funcionario
    form = Funcionario
    fields = "__all__"  
    success_message = 'Funcionario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar 
 
    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):               
        return reverse('funcionario') # Redireccionamos a la vista principal 'leer' 
 
class FuncionarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Funcionario 
    form = Funcionario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self): 
        success_message = 'Funcionario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un 
        messages.success (self.request, (success_message))       
        return reverse('funcionario') # Redireccionamos a la vista principal 'leer'