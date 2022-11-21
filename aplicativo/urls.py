from django.urls import path, re_path

from .views_tela.anuncio_view import *
from .views_tela.imoveis_view import *
from .views_tela.reserva_view import *



urlpatterns = [
    # ------------------Anuncios---------------
    path('anuncios/', index_anuncio, name='index'),
    path('cadastro_anuncio/', cadastro_anuncio, name='tela_cadastro_anuncio'),
    path('editar_anuncio/<str:id>', editar_anuncio, name='editar_anuncio'),
    # --------------------Api----------------
    re_path('api-busca_anuncio/(?P<id>\w+|)', AnunciosAPI, name='busca_anuncio'),
    path('api-cadastro_anuncio/', AddAnunciosAPI, name='cadastro_anuncio_'),
    path('editar/anuncio/<str:id>', UpdateAnuncio, name='UpdateAnuncio'),
    path('delete/anuncio/<str:id>', DeleteAnuncio, name='DeleteAnuncio'),
    






    # ------------------Imoveis---------------
    path('', index_imoves, name='index_imoveis'),
    path('cadastro_imoveis', cadastro_imoves, name='cadastro_imoveis'),
    path('editar_imovel/<str:id>', editar_imovel, name='editar_imovel'),
    # --------------Api------------------
    path('api/cadastro_imoveis/', AddImoveisAPI, name='AddImoveisAPI'),
    re_path('buscar/imoveis/(?P<id>\w+|)', ImoveisAPI, name='ImoveisAPI'),
    path('editar/imovel/<str:id>', ImovelUpdate, name='ImovelUpdate'),
    path('delete/imovel/<str:id>', ImovelDelete, name='ImovelDelete'),




    # ------------------Reservas---------------
    path('reservas/', index_reserva, name='index_reservas'),
    path('cadastro_reservas/', cadastro_reserva, name='tela_cadastro_reservas'),
    path('editar_reservas/<str:id>', editar_reserva, name='editar_reservas'),
    # ---------------------API---------------
    re_path('api-busca_reservas/(?P<id>\w+|)',ReservasAPI, name='busca_reservas'),
    path('api-cadastro_reservas/', AddReservasAPI, name='cadastro_reservas_'),
    path('delete/reservas/<str:id>', DeleteReservas, name='Deletereservas'),
    


]