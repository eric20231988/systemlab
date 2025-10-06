from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from ..models import Analisis
from ..forms import AnalisisForm

# -------------------- LISTAR --------------------

def listar_analisis(request):
    analisis_list = Analisis.objects.all().order_by('nombre')
    paginator = Paginator(analisis_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "analisis/base_analisis/listar.html", {
        "page_obj": page_obj
    })

# -------------------- CREAR --------------------

def crear_analisis(request):
    form = AnalisisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("analisis:listar_analisis")
    return render(request, "analisis/base_analisis/crear_analisis.html", {
        "form": form
    })

# -------------------- EDITAR --------------------

def editar_analisis(request, pk):
    analisis = get_object_or_404(Analisis, pk=pk)
    form = AnalisisForm(request.POST or None, instance=analisis)
    if form.is_valid():
        form.save()
        return redirect("analisis:listar_analisis")
    return render(request, "analisis/base_analisis/editar_analisis.html", {
        "form": form,
        "analisis": analisis
    })

# -------------------- ELIMINAR --------------------

def eliminar_analisis(request, pk):
    analisis = get_object_or_404(Analisis, pk=pk)
    if request.method == "POST":
        if not analisis.perfiles.exists():
            analisis.delete()
        return redirect("analisis:listar_analisis")
    return render(request, "analisis/base_analisis/eliminar_analisis.html", {
        "analisis": analisis
    })

# -------------------- DETALLE --------------------

def detalle_analisis(request, pk):
    analisis = get_object_or_404(Analisis, pk=pk)
    return render(request, "analisis/base_analisis/detalle.html", {
        "analisis": analisis
    })
