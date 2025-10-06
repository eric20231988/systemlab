from django.shortcuts import render, get_object_or_404, redirect
from ..models import CategoriaExamen
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaExamen
        fields = '__all__'

def listar_categorias(request):
    categorias = CategoriaExamen.objects.all()
    return render(request, 'examenes/listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('examenes:listar_categorias')
    return render(request, 'examenes/crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(CategoriaExamen, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('examenes:listar_categorias')
    return render(request, 'examenes/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(CategoriaExamen, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('examenes:listar_categorias')
    return render(request, 'examenes/eliminar_categoria.html', {'categoria': categoria})
