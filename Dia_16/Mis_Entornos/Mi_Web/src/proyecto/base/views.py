from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea
# Create your views here.
'''def lista_pendientes(pedido):
    return HttpResponse('Lista de Pendientes')'''

class Logueo(LoginView):
    template_name ="base/Login.html"
    field = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('pendientes')
    
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url= reverse_lazy('pendientes')
    #para que quede logueado una vez se registre
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request,usuario)

        return super(PaginaRegistro,self).form_valid(form)
    def get(self,*arg,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('pendientes')
        return super(PaginaRegistro, self).get(*arg,**kwargs)


class ListaPendientes(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = 'tareas'
    #para mostrar elementos por usuario
    def get_context_data(self,**kwarg):
        contexto = super().get_context_data(**kwarg)
        contexto['tareas']=contexto['tareas'].filter(usuario=self.request.user)
        contexto['count']=contexto['tareas'].filter(completo=False).count()
        #para buscar en la caja de texto
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            contexto['tareas'] = contexto['tareas'].filter(titulo__icontains=valor_buscado)
            contexto['valor_buscado'] = valor_buscado
        return contexto

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    #para cambiar el nombre al que uno elija
    template_name='base/tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model =  Tarea
    fields = ['titulo','descripcion', 'completo']
    success_url= reverse_lazy('pendientes')

    def form_valid(self, form):
        form.instance.usuario =self.request.user
        return super(CrearTarea,self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    model =  Tarea
    #fields = '__all__'
    fields = ['titulo','descripcion', 'completo']
    success_url= reverse_lazy('pendientes')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model =  Tarea
    context_object_name = 'tarea'
    success_url= reverse_lazy('pendientes')