from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView 


urlpatterns = [
    path('', views.index, name='index'), 
    path('sitio_web/', views.sitio_web, name='sitio_web'), 
    path('alas_de_hierro/', views.alas_de_hierro, name='alas_de_hierro'), 
    path('alas_de_onix/', views.alas_de_onix, name='alas_de_onix'), 
    path('alas_de_sangre/', views.alas_de_sangre, name='alas_de_sangre'), 
    
    path('Avalier 1.El último rey dragón/', views.Avalier_1_El_último_rey_dragón, name='Avalier 1.El último rey dragón'),
    
    path('avalier_1_el_ultimo_rey_dragon/', views.avalier_1_el_ultimo_rey_dragon, name='avalier_1_el_ultimo_rey_dragon'),
    path('avalier_2_el_desolado_rey_elfo/', views.avalier_2_el_desolado_rey_elfo, name='avalier_2_el_desolado_rey_elfo'),
    path('black_clover/', views.black_clover, name='black_clover'),
    path('boku_no_hero_academia/', views.boku_no_hero_academia, name='boku_no_hero_academia'),
    path('el_cautivo_rey_lobo/', views.el_cautivo_rey_lobo, name='el_cautivo_rey_lobo'),
    path('el_despiadado_rey_fae/', views.el_despiadado_rey_fae, name='el_despiadado_rey_fae'),
    path('en_busca_de_los_elementales/', views.en_busca_de_los_elementales, name='en_busca_de_los_elementales'),
    path('kaiju_no_8/', views.kaiju_no_8, name='kaiju_no_8'),
    path('kimetsu_no_yaiba/', views.kimetsu_no_yaiba, name='kimetsu_no_yaiba'),
    path('one_piece/', views.one_piece, name='one_piece'),
    
    path('libros/', views.libro_index, name='libro_index'),
    path('manga/', views.manga_index, name='manga_index'),
    path('novela/', views.novela_index, name='novela_index'),
    
]