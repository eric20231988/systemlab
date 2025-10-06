from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from .forms import PacienteForm
from .models import Paciente
from .selectors import pacientes_queryset
from .services import crear_paciente, actualizar_paciente, eliminar_paciente


@method_decorator(
    [login_required, permission_required('pacientes.view_paciente', raise_exception=True)],
    name='dispatch'
)
class PacienteListView(View):
    template_name = 'pacientes/list.html'

    def get(self, request):
        pacientes = pacientes_queryset('')
        return render(request, self.template_name, {'pacientes': pacientes})


@login_required
@permission_required('pacientes.view_paciente', raise_exception=True)
def tabla_pacientes(request):
    q = request.GET.get('q', '').strip()
    pacientes = pacientes_queryset(q)
    return render(request, 'pacientes/partials/table_with_message.html', {
        'pacientes': pacientes,
        'mensaje': None,
        'tipo_mensaje': None
    })


@login_required
@permission_required('pacientes.add_paciente', raise_exception=True)
def crear_paciente_view(request):
    form = PacienteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        crear_paciente(form)
        pacientes = pacientes_queryset('')

        if request.headers.get('HX-Request') == 'true':
            # devolvemos el panel_list completo (no solo la tabla)
            response = render(request, 'pacientes/partials/panel_list.html', {
                'pacientes': pacientes,
            })
            # trigger para limpiar el form-container y restaurar layout
            response['HX-Trigger'] = 'pacienteGuardado'
            return response

        # flujo normal (no HTMX)
        return redirect('pacientes:listar')

    # si es HTMX y no es válido, devolvemos solo el form parcial
    if request.headers.get('HX-Request') == 'true':
        return render(request, 'pacientes/partials/form.html', {
            'form': form,
            'paciente': None
        })

    # render normal
    return render(request, 'pacientes/create.html', {'form': form})



@login_required
@permission_required('pacientes.change_paciente', raise_exception=True)
def editar_paciente_view(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST' and form.is_valid():
        actualizar_paciente(form)
        pacientes = pacientes_queryset('')
        if request.headers.get('HX-Request') == 'true':
            # devolvemos el panel_list completo
            response = render(request, 'pacientes/partials/panel_list.html', {
                'pacientes': pacientes,
            })
            # trigger para limpiar el form-container y restaurar layout
            response['HX-Trigger'] = 'pacienteGuardado'
            return response
        return redirect('pacientes:detalle', pk=paciente.pk)

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'pacientes/partials/form.html', {'form': form, 'paciente': paciente})

    return render(request, 'pacientes/update.html', {'form': form, 'paciente': paciente})



@login_required
@permission_required('pacientes.delete_paciente', raise_exception=True)
def eliminar_paciente_view(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        eliminar_paciente(paciente)
        pacientes = pacientes_queryset('')

        if request.headers.get('HX-Request') == 'true':
            # Devolvemos el panel_list completo para la izquierda
            response = render(request, 'pacientes/partials/panel_list.html', {
                'pacientes': pacientes,
            })
            # Disparamos evento para limpiar el form-container y restaurar layout
            response['HX-Trigger'] = 'pacienteGuardado'
            return response

        # Flujo normal (no HTMX)
        return redirect('pacientes:listar')

    # Render de confirmación
    if request.headers.get('HX-Request') == 'true':
        return render(request, 'pacientes/partials/delete_confirm.html', {'paciente': paciente})
    return render(request, 'pacientes/delete.html', {'paciente': paciente})



@method_decorator(
    [login_required, permission_required('pacientes.view_paciente', raise_exception=True)],
    name='dispatch'
)
class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'pacientes/detail.html'
    context_object_name = 'paciente'

    def render_to_response(self, context, **response_kwargs):
        request = self.request
        if request.headers.get('HX-Request') == 'true':
            return render(request, 'pacientes/partials/detail_card.html', context)
        return super().render_to_response(context, **response_kwargs)


@login_required
@permission_required('pacientes.view_paciente', raise_exception=True)
def verificar_dni(request):
    dni = request.GET.get('dni', '').strip()
    pacientes = pacientes_queryset('')
    if not dni:
        return render(request, 'pacientes/partials/_resultado_vacio.html', {'pacientes': pacientes})
    paciente = Paciente.objects.filter(dni=dni).first()
    if paciente:
        return render(request, 'pacientes/partials/_paciente_registrado.html', {
            'paciente': paciente,
            'pacientes': pacientes
        })
    return render(request, 'pacientes/partials/_paciente_no_registrado.html', {
        'dni': dni,
        'pacientes': pacientes
    })


@login_required
@permission_required('pacientes.view_paciente', raise_exception=True)
def panel_list_partial(request):
    pacientes = pacientes_queryset('')
    return render(request, 'pacientes/partials/panel_list.html', {'pacientes': pacientes})
