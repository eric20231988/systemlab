from django.shortcuts import render, get_object_or_404, redirect
from ..models import Examen
from ..forms import ExamenForm
from django.core.paginator import Paginator

def listar_examenes(request):
    examenes = Examen.objects.select_related('categoria').prefetch_related('analisis')
    paginator = Paginator(examenes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'examenes/listar.html', {'page_obj': page_obj})

def crear_examen(request):
    form = ExamenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('examenes:listar')
    return render(request, 'examenes/crear.html', {'form': form})

def editar_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    form = ExamenForm(request.POST or None, instance=examen)
    if form.is_valid():
        form.save()
        return redirect('examenes:listar')
    return render(request, 'examenes/editar.html', {'form': form})

def eliminar_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    if request.method == 'POST':
        examen.delete()
        return redirect('examenes:listar')
    return render(request, 'examenes/eliminar.html', {'examen': examen})

def detalle_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    total = examen.calcular_total()
    return render(request, 'examenes/detalle.html', {'examen': examen, 'total': total})
