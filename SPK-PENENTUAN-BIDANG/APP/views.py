from django.shortcuts import render, redirect,get_object_or_404
from .models import Alternatif, Kriteria, Gap
from .forms import AlternatifForm, KriteriaForm

def index(request):
    
    return render(request,'index.html')

def alternatif(request):

    datas = Alternatif.objects.all()
    return render(request,'alternatif.html', {'datas':datas})

def create_alternatif(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:alternatif')
    else:
        form = AlternatifForm()

    return render(request, 'alternatif_create.html', {'form': form})

def update_alternatif(request, pk):
    alternatif = get_object_or_404(Alternatif, pk=pk)

    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            return redirect('dashboard:alternatif')
    else:
        form = AlternatifForm(instance=alternatif)

    return render(request, 'alternatif_create.html', {'form': form, 'alternatif': alternatif})

def delete_alternatif(request, pk):
    alternatif = get_object_or_404(Alternatif, pk=pk)
    alternatif.delete()
    return redirect('dashboard:alternatif')


# CRITERIA
def kriteria(request):

    datas = Kriteria.objects.all()
    return render(request,'kriteria.html', {'datas':datas})

def create_kriteria(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:kriteria')
    else:
        form = KriteriaForm()

    return render(request, 'kriteria_create.html', {'form': form})

def update_kriteria(request, pk):
    kriteria = get_object_or_404(Kriteria, pk=pk)

    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('dashboard:kriteria')
    else:
        form = KriteriaForm(instance=kriteria)

    return render(request, 'kriteria_create.html', {'form': form, 'kriteria': kriteria})

def delete_kriteria(request, pk):
    kriteria = get_object_or_404(Kriteria, pk=pk)
    kriteria.delete()
    return redirect('dashboard:kriteria')