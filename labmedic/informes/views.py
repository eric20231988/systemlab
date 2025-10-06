from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Informe
from .forms import InformeForm
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import DeleteView

class InformeListView(ListView):
    model = Informe
    template_name = 'informes/listar.html'
    context_object_name = 'informes'
    paginate_by = 20

class InformeDetailView(DetailView):
    model = Informe
    template_name = 'informes/detalle.html'
    context_object_name = 'informe'

class InformeCreateView(CreateView):
    model = Informe
    form_class = InformeForm
    template_name = 'informes/crear.html'
    success_url = reverse_lazy('informes:listar')

class InformeUpdateView(UpdateView):
    model = Informe
    form_class = InformeForm
    template_name = 'informes/editar.html'
    success_url = reverse_lazy('informes:listar')

def generar_pdf_informe(request, pk):
    informe = Informe.objects.get(pk=pk)
    resultados = informe.registro_examen.resultadoanalito_set.select_related('analito')
    html_string = render_to_string('informes/generar_pdf.html', {
        'informe': informe,
        'resultados': resultados
    })
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="informe_{informe.pk}.pdf"'
    return response
class InformeDeleteView(DeleteView):
    model = Informe
    template_name = 'informes/eliminarinforme.html'
    success_url = reverse_lazy('informes:listar')

def enviar_por_whatsapp(request, pk):
    informe = get_object_or_404(Informe, pk=pk)
    return render(request, 'informes/enviar_por_whatsapp.html', {'informe': informe})

