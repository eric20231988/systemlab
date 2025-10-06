from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from analitos.models import Analito
from analisis.models import Analisis, PerfilAnalisis
from examen.models import TipoExamen
from resultados_analitos.models import ResultadoAnalito
from registrar_examenes.models import RegistroExamen

# Vista principal del panel
class PanelLaboratorioView(LoginRequiredMixin, TemplateView):
    template_name = 'laboratorio/panel.html'


# Vistas para listar analitos
class AnalitosListView(LoginRequiredMixin, ListView):
    model = Analito
    template_name = 'laboratorio/analitos_listar.html'
    context_object_name = 'analitos'
    paginate_by = 20


# Vistas para listar análisis
class AnalisisListView(LoginRequiredMixin, ListView):
    model = Analisis
    template_name = 'laboratorio/analisis_listar.html'
    context_object_name = 'analisis'
    paginate_by = 20


# Vistas para listar exámenes
class ExamenesListView(LoginRequiredMixin, ListView):
    model = TipoExamen
    template_name = 'laboratorio/examenes_listar.html'
    context_object_name = 'examenes'
    paginate_by = 20


# Vistas para listar resultados
class ResultadosListView(LoginRequiredMixin, ListView):
    model = ResultadoAnalito
    template_name = 'laboratorio/resultados_listar.html'
    context_object_name = 'resultados'
    paginate_by = 20

    def get_queryset(self):
        return ResultadoAnalito.objects.select_related('registro_examen', 'analito').order_by('-fecha_registro')


# Vistas para listar órdenes de examen
class OrdenExamenListView(LoginRequiredMixin, ListView):
    model = RegistroExamen
    template_name = 'laboratorio/orden_examen_listar.html'
    context_object_name = 'ordenes'
    paginate_by = 20

    def get_queryset(self):
        return RegistroExamen.objects.select_related('paciente', 'tipo_examen').order_by('-fecha_creacion')
