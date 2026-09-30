from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Vista para que un usuario nuevo se registre
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

# --- PROYECTOS ---

class ListaProyectos(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'tareas/lista_proyectos.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        # Solo muestra los proyectos del usuario logeado
        return Proyecto.objects.filter(usuario=self.request.user)


class DetalleProyecto(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'tareas/detalle_proyecto.html'
    context_object_name = 'proyecto'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class CrearProyecto(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'tareas/form_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def form_valid(self, form):
        # Asigna automáticamente el usuario logeado como dueño del proyecto
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EditarProyecto(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'tareas/form_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class EliminarProyecto(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'tareas/confirmar_eliminar_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


# --- TAREAS ---

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/form_tarea.html'

    def form_valid(self, form):
        # Asocia la tarea al proyecto indicado en la URL
        proyecto = Proyecto.objects.get(pk=self.kwargs['proyecto_id'], usuario=self.request.user)
        form.instance.proyecto = proyecto
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalle_proyecto', kwargs={'pk': self.kwargs['proyecto_id']})


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/form_tarea.html'

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy('detalle_proyecto', kwargs={'pk': self.object.proyecto.pk})


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tareas/confirmar_eliminar_tarea.html'

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy('detalle_proyecto', kwargs={'pk': self.object.proyecto.pk})