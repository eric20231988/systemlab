from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Especialidad
from .forms import EspecialidadForm
from django.views.generic import DeleteView
from django.shortcuts import redirect
from django.contrib import messages


class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'especialidad/listar.html'
    context_object_name = 'especialidades'
    paginate_by = 20

class EspecialidadDetailView(DetailView):
    model = Especialidad
    template_name = 'especialidad/detalle.html'
    context_object_name = 'especialidad'

class EspecialidadCreateView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad/crear.html'
    success_url = reverse_lazy('especialidad:listar')

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad/editar.html'
    success_url = reverse_lazy('especialidad:listar')


class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'especialidad/confirmar_eliminar.html'
    success_url = reverse_lazy('especialidad:listar')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Validación opcional: evitar eliminar si está vinculada a médicos
        if hasattr(self.object, 'medico_set') and self.object.medico_set.exists():
            messages.error(request, "❌ No se puede eliminar: esta especialidad está asignada a médicos.")
            return redirect('especialidad:detalle', pk=self.object.pk)
        return super().delete(request, *args, **kwargs)
