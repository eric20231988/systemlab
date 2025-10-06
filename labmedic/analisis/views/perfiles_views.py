from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from ..models import PerfilAnalisis
from ..forms import PerfilAnalisisForm

def listar_perfiles(request):
    query = request.GET.get("q", "")
    tipo = request.GET.get("tipo", "")
    perfiles = PerfilAnalisis.objects.prefetch_related("analisis")

    if query:
        perfiles = perfiles.filter(nombre__icontains=query)
    if tipo:
        perfiles = perfiles.filter(descripcion__icontains=tipo)

    paginator = Paginator(perfiles, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "analisis/base_analisis/lista_perfiles.html", {
        "page_obj": page_obj,
        "query": query,
        "tipo": tipo
    })

def crear_perfil(request):
    form = PerfilAnalisisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("analisis:listar_perfiles")
    return render(request, "analisis/base_analisis/crear_perfiles.html", {"form": form})

def editar_perfil(request, pk):
    perfil = get_object_or_404(PerfilAnalisis, pk=pk)
    form = PerfilAnalisisForm(request.POST or None, instance=perfil)
    if form.is_valid():
        form.save()
        return redirect("analisis:listar_perfiles")
    return render(request, "analisis/base_analisis/editar_perfiles.html", {"form": form})

def eliminar_perfil(request, pk):
    perfil = get_object_or_404(PerfilAnalisis, pk=pk)
    if request.method == "POST":
        perfil.delete()
        return redirect("analisis:listar_perfiles")
    return render(request, "analisis/base_analisis/eliminar_perfiles.html", {"perfil": perfil})

def detalle_perfil(request, pk):
    perfil = get_object_or_404(PerfilAnalisis, pk=pk)
    return render(request, "analisis/base_analisis/detalle_perfil.html", {"perfil": perfil})
