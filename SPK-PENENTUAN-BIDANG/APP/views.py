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

    hasil_perhitungan = {}
    for kriteria in kriterias:
 
        nilai_target = kriteria.nilai_target
        hasil_pengurangan = []

        for penilaian in penilaians:
            nilai_kriteria = getattr(penilaian, f'penilaian_kriteria{kriteria.pk}')
            hasil_pengurangan.append(nilai_kriteria - nilai_target)

        hasil_perhitungan[kriteria.nama_kriteria] = hasil_pengurangan

    konversi_hasil_perhitungan = {}
    for kriteria in kriterias:
        nilai_target = kriteria.nilai_target
        konversi_hasil_pengurangan = []
        for penilaian in penilaians:
            nilai_kriteria = getattr(penilaian, f'penilaian_kriteria{kriteria.pk}')
            hasil = nilai_kriteria - nilai_target
            if hasil == 0:
                konversi_hasil_pengurangan.append(5)
            elif hasil == 1:
                konversi_hasil_pengurangan.append(4.5)
            elif hasil == -1:
                konversi_hasil_pengurangan.append(4)
            elif hasil == 2:
                konversi_hasil_pengurangan.append(3.5)
            elif hasil == -2:
                konversi_hasil_pengurangan.append(3)
            elif hasil == 3:
                konversi_hasil_pengurangan.append(2.5)
            elif hasil == -3:
                konversi_hasil_pengurangan.append(2)
            elif hasil == 4:
                konversi_hasil_pengurangan.append(1.5)
            elif hasil == -4:
                konversi_hasil_pengurangan.append(1)
        konversi_hasil_perhitungan[kriteria.nama_kriteria] = konversi_hasil_pengurangan

    print(konversi_hasil_perhitungan)
    
    # nilai rata-rata core factor
    tes1_values = konversi_hasil_perhitungan['TES 1 ( PENGETAHUAN DASAR )']
    tes2_values = konversi_hasil_perhitungan['TES 2 ( LOGIKA MATEMATIKA )']
    # nilai rata-rata secondery factor
    tes3_values = konversi_hasil_perhitungan['TES 3 ( PENGETAHUAN PROGRAMMING )']
    tes4_values = konversi_hasil_perhitungan['TES 4 ( PENGETAHUAN JARINGAN & IOT )']
    tes5_values = konversi_hasil_perhitungan['TES 5 ( PENGETAHUAN MULTIMEDIA )']

    print("TES 1 Values:", tes1_values)
    print("TES 2 Values:", tes2_values)

    print("TES 3 Values:", tes3_values)
    print("TES 4 Values:", tes4_values)
    print("TES 5 Values:", tes5_values)

    hasil_avarage_cf = []
    hasil_avarage_sf = []

    for x in range(len(tes1_values)):
        # CF
        a = float(tes1_values[x])
        b = float(tes2_values[x])
        data_cf = (a+b)/2

        hasil_avarage_cf.append(round(data_cf, 2))
        # SF
        c = float(tes3_values[x])
        d = float(tes4_values[x])
        e = float(tes5_values[x])
        data_sf = (c+d+e)/3

        hasil_avarage_sf.append(round(data_sf, 2))
        
    print("CORE FACTOR",hasil_avarage_cf)
    print("SECONDERY FACTOR",hasil_avarage_sf)

    nilaia_total = []

    for x in range(len(hasil_avarage_cf)):

        nt_cf = (60/100)* hasil_avarage_cf[x]
        nt_sf = (40/100)* hasil_avarage_sf[x]

        nt = nt_cf + nt_sf
        nilaia_total.append(round(nt,2))
       
    print("nilai total = ", nilaia_total)
  

    context = {
        'nilaia_total':nilaia_total,
        'hasil_avarage_cf':hasil_avarage_cf,
        'hasil_avarage_sf':hasil_avarage_sf,
        'penilaian':penilaians,
        'penilaias':penilaians,
        'alternatif':alternatif,
        'kriteria':kriterias,
        'hasil_perhitungan': hasil_perhitungan,
        'konversi_hasil_perhitungan': konversi_hasil_perhitungan,
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