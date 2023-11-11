from django.urls import path
from .import views
app_name="APP"

urlpatterns = [
    path('', views.index, name='index'),
    path('alternatif/', views.alternatif, name='alternatif'),
    path('alternatif/create/', views.create_alternatif, name='create_alternatif'),
    path('alternatif/update/<int:pk>', views.update_alternatif, name='update_alternatif'),
    path('alternatif/delete/<int:pk>', views.delete_alternatif, name='delete_alternatif'),
    # kriteria
    path('kriteria/', views.kriteria, name='kriteria'),
    path('kriteria/create/', views.create_kriteria, name='create_kriteria'),
    path('kriteria/update/<int:pk>', views.update_kriteria, name='update_kriteria'),
    path('kriteria/delete/<int:pk>', views.delete_kriteria, name='delete_kriteria'),
    # kriteria
]
