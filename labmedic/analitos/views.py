from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Analito
from .forms import AnalitoForm

class AnalitoListView(ListView):
    model = Analito
    template_name = 'analitos/listar.html'
    context_object_name = 'analitos'
    paginate_by = 20

class AnalitoDetailView(DetailView):
    model = Analito
    template_name = 'analitos/detalle.html'
    context_object_name = 'analito'

class AnalitoCreateView(CreateView):
    model = Analito
    form_class = AnalitoForm
    template_name = 'analitos/crear.html'
    success_url = reverse_lazy('analitos:listar')

class AnalitoUpdateView(UpdateView):
    model = Analito
    form_class = AnalitoForm
    template_name = 'analitos/editar.html'
    success_url = reverse_lazy('analitos:listar')
