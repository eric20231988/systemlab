from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import pandas as pd

from .models import RegistroExamen
from .forms import RegistroExamenForm
from .filters import RegistroExamenFilter


class RegistroExamenListView(FilterView):
    model = RegistroExamen
    template_name = 'registrar_examenes/listar.html'
    context_object_name = 'examenes'
    filterset_class = RegistroExamenFilter
    paginate_by = 20


class RegistroExamenDetailView(DetailView):
    model = RegistroExamen
    template_name = 'registrar_examenes/detalle.html'
    context_object_name = 'examen'


class RegistroExamenCreateView(CreateView):
    model = RegistroExamen
    form_class = RegistroExamenForm
    template_name = 'registrar_examenes/crear.html'
    success_url = reverse_lazy('registrar_examenes:listar_general')  # corregido

    def form_valid(self, form):
        form.instance.registrado_por = self.request.user
        return super().form_valid(form)


class RegistroExamenUpdateView(UpdateView):
    model = RegistroExamen
    form_class = RegistroExamenForm
    template_name = 'registrar_examenes/editar.html'
    success_url = reverse_lazy('registrar_examenes:listar_general')  # corregido


class RegistroExamenDeleteView(DeleteView):
    model = RegistroExamen
    template_name = 'registrar_examenes/confirmar_eliminar.html'
    success_url = reverse_lazy('registrar_examenes:listar_general')  # corregido


def exportar_excel(request):
    registros = RegistroExamen.objects.all()
    df = pd.DataFrame(registros.values('paciente', 'tipo_examen__nombre', 'estado', 'fecha_creacion'))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="examenes.xlsx"'
    df.to_excel(response, index=False)
    return response


def exportar_pdf(request):
    registros = RegistroExamen.objects.all().order_by('-fecha_creacion')
    html_string = render_to_string('registrar_examenes/pdf_examenes.html', {'registros': registros})
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ordenes_examen.pdf"'
    return response


# Vista funcional para compatibilidad con urls.py
listar = RegistroExamenListView.as_view()
