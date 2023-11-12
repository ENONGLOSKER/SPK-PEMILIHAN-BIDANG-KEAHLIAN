# forms.py
from django import forms
from .models import Alternatif,Kriteria,Gap, Penilaian

class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = ['nama_alternatif', 'simbol', 'nim', 'alamat']
        widgets = {
            'nama_alternatif': forms.TextInput(attrs={'class': 'form-control'}),
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nama_alternatif = cleaned_data.get('nama_alternatif')
        simbol = cleaned_data.get('simbol')
        nim = cleaned_data.get('nim')
        alamat = cleaned_data.get('alamat')

        cleaned_data['nama_alternatif'] = nama_alternatif.upper() if nama_alternatif else None
        cleaned_data['simbol'] = simbol.upper() if simbol else None
        cleaned_data['nim'] = nim.upper() if nim else None
        cleaned_data['alamat'] = alamat.upper() if alamat else None

        return cleaned_data

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields =  ['nama_kriteria', 'nilai_target']
        widgets = {
            'nama_kriteria': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai_target': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nama_kriteria = cleaned_data.get('nama_kriteria')
        cleaned_data['nama_kriteria'] = nama_kriteria.upper() if nama_kriteria else None

        return cleaned_data

class GapForm(forms.ModelForm):
    class Meta:
        model = Gap
        fields =  ['nilai', 'gap']
        widgets = {
            'nilai': forms.TextInput(attrs={'class': 'form-control'}),
            'gap': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PenilaianForm(forms.ModelForm):
    nilai_kriteria_CHOICES = [
            ('0','0'),
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
        ]
    penilaian_kriteria1 = forms.ChoiceField(choices=nilai_kriteria_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    penilaian_kriteria2 = forms.ChoiceField(choices=nilai_kriteria_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    penilaian_kriteria3 = forms.ChoiceField(choices=nilai_kriteria_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    penilaian_kriteria4 = forms.ChoiceField(choices=nilai_kriteria_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    penilaian_kriteria5 = forms.ChoiceField(choices=nilai_kriteria_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Penilaian
        fields =  ['penilaian_alternatif', 'penilaian_kriteria1', 'penilaian_kriteria2', 'penilaian_kriteria3', 'penilaian_kriteria4', 'penilaian_kriteria5']
        widgets = {
            'penilaian_alternatif': forms.Select(attrs={'class': 'form-control'}),
            'penilaian_kriteria1': forms.NumberInput(attrs={'class': 'form-control'}),
            'penilaian_kriteria2': forms.NumberInput(attrs={'class': 'form-control'}),
            'penilaian_kriteria3': forms.NumberInput(attrs={'class': 'form-control'}),
            'penilaian_kriteria4': forms.NumberInput(attrs={'class': 'form-control'}),
            'penilaian_kriteria5': forms.NumberInput(attrs={'class': 'form-control'}),
        }
