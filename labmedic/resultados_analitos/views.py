from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ResultadoAnalito
from .forms import ResultadoAnalitoForm
from .services import evaluar_estado
from django.contrib import messages

class ResultadoListView(ListView):
    model = ResultadoAnalito
    template_name = 'resultados_analitos/listar.html'
    context_object_name = 'resultados'
    paginate_by = 20

class ResultadoDetailView(DetailView):
    model = ResultadoAnalito
    template_name = 'resultados_analitos/detalle.html'
    context_object_name = 'resultado'

class ResultadoCreateView(CreateView):
    model = ResultadoAnalito
    form_class = ResultadoAnalitoForm
    template_name = 'resultados_analitos/crear.html'
    success_url = reverse_lazy('resultados_analitos:listar')

    def form_valid(self, form):
        resultado = form.save(commit=False)
        resultado.estado = evaluar_estado(resultado.valor, resultado.analito)
        resultado.save()
        return super().form_valid(form)

class ResultadoUpdateView(UpdateView):
    model = ResultadoAnalito
    form_class = ResultadoAnalitoForm
    template_name = 'resultados_analitos/editar.html'
    success_url = reverse_lazy('resultados_analitos:listar')

    def form_valid(self, form):
        resultado = form.save(commit=False)
        resultado.estado = evaluar_estado(resultado.valor, resultado.analito)
        resultado.save()
        return super().form_valid(form)

class ResultadoDeleteView(DeleteView):
    model = ResultadoAnalito
    template_name = 'resultados_analitos/elimina_resultados.html'
    success_url = reverse_lazy('resultados_analitos:listar')
