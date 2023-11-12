from django.shortcuts import render, redirect,get_object_or_404
from .models import Alternatif, Kriteria, Gap, Penilaian
from .forms import AlternatifForm, KriteriaForm, GapForm, PenilaianForm

def index(request):
    
    return render(request,'index.html')
# penilaian
def penilaian(request):
    alternatif = Alternatif.objects.all()
    kriterias = Kriteria.objects.all()
    penilaians = Penilaian.objects.all()

    # Inisialisasi dictionary untuk menyimpan hasil perhitungan
    hasil_perhitungan = {}

    # Looping untuk setiap kriteria
    for kriteria in kriterias:
 
        nilai_target = kriteria.nilai_target
        hasil_pengurangan = []

        # Looping untuk setiap data penilaian
        for penilaian in penilaians:
            # Ambil nilai kriteria untuk penilaian tertentu
            nilai_kriteria = getattr(penilaian, f'penilaian_kriteria{kriteria.pk}')
            # print(nilai_kriteria)
            # Hitung hasil pengurangan
            hasil_pengurangan.append(nilai_kriteria - nilai_target)

        # Simpan hasil pengurangan ke dictionary
        hasil_perhitungan[kriteria.nama_kriteria] = hasil_pengurangan

    context = {
        'penilaian':penilaians,
        'penilaias':penilaians,
        'alternatif':alternatif,
        'kriteria':kriterias,
        'hasil_perhitungan': hasil_perhitungan,
    }
    
    return render(request,'penilaian.html',context)

def create_penilaian(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:penilaian')
    else:
        form = PenilaianForm()

    return render(request, 'penilaian_create.html', {'form': form})

def update_penilaian(request, pk):
    penilaian = get_object_or_404(Penilaian, pk=pk)

    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('dashboard:penilaian')
    else:
        form = PenilaianForm(instance=penilaian)

    return render(request, 'penilaian_create.html', {'form': form, 'penilaian': penilaian})

def delete_penilaian(request, pk):
    penilaian = get_object_or_404(Penilaian, pk=pk)
    penilaian.delete()
    return redirect('dashboard:penilaian')

# alternatif
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

# GAP
def gap(request):

    datas = Gap.objects.all()
    return render(request,'gap.html', {'datas':datas})

def create_gap(request):
    if request.method == 'POST':
        form = GapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:gap')
    else:
        form = GapForm()

    return render(request, 'gap_create.html', {'form': form})

def update_gap(request, pk):
    gap = get_object_or_404(Gap, pk=pk)

    if request.method == 'POST':
        form = GapForm(request.POST, instance=gap)
        if form.is_valid():
            form.save()
            return redirect('dashboard:gap')
    else:
        form = GapForm(instance=gap)

    return render(request, 'gap_create.html', {'form': form, 'gap': gap})

def delete_gap(request, pk):
    gap = get_object_or_404(Gap, pk=pk)
    gap.delete()
    return redirect('dashboard:gap')