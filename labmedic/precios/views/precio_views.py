# precios/views/precio_views.py
from django.shortcuts import render, get_object_or_404, redirect
from ..models import PrecioAnalisis
from ..forms import PrecioAnalisisForm
from django.core.paginator import Paginator

def listar_precios(request):
    precios = PrecioAnalisis.objects.select_related('analisis').order_by('-fecha_inicio')
    paginator = Paginator(precios, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'precios/listar.html', {'page_obj': page_obj})

def crear_precio(request):
    form = PrecioAnalisisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('precios:listar')
    return render(request, 'precios/crear.html', {'form': form})

def editar_precio(request, pk):
    precio = get_object_or_404(PrecioAnalisis, pk=pk)
    form = PrecioAnalisisForm(request.POST or None, instance=precio)
    if form.is_valid():
        form.save()
        return redirect('precios:listar')
    return render(request, 'precios/editar.html', {'form': form})

def eliminar_precio(request, pk):
    precio = get_object_or_404(PrecioAnalisis, pk=pk)
    if request.method == 'POST':
        precio.delete()
        return redirect('precios:listar')
    return render(request, 'precios/eliminar.html', {'precio': precio})

def detalle_precio(request, pk):
    precio = get_object_or_404(PrecioAnalisis, pk=pk)
    return render(request, 'precios/detalle.html', {'precio': precio})
