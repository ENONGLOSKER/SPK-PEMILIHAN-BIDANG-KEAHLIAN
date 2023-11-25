from django.urls import path
from .import views
app_name="APP"

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alternatif/', views.alternatif, name='alternatif'),
    path('alternatif/create/', views.create_alternatif, name='create_alternatif'),
    path('alternatif/update/<int:pk>', views.update_alternatif, name='update_alternatif'),
    path('alternatif/delete/<int:pk>', views.delete_alternatif, name='delete_alternatif'),
    # kriteria
    path('kriteria/', views.kriteria, name='kriteria'),
    path('kriteria/create/', views.create_kriteria, name='create_kriteria'),
    path('kriteria/update/<int:pk>', views.update_kriteria, name='update_kriteria'),
    path('kriteria/delete/<int:pk>', views.delete_kriteria, name='delete_kriteria'),
    # gap
    path('gap/', views.gap, name='gap'),
    path('gap/create/', views.create_gap, name='create_gap'),
    path('gap/update/<int:pk>', views.update_gap, name='update_gap'),
    path('gap/delete/<int:pk>', views.delete_gap, name='delete_gap'),
    # penilaian
    path('penilaian/', views.penilaian, name='penilaian'),
    path('penilaian/create/', views.create_penilaian, name='create_penilaian'),
    path('penilaian/update/<int:pk>', views.update_penilaian, name='update_penilaian'),
    path('penilaian/delete/<int:pk>', views.delete_penilaian, name='delete_penilaian'),
]
