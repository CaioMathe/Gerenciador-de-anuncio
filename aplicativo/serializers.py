from rest_framework import serializers
from .models import Imoveis, Anuncios, Reservas

class ImoveisSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    limite_hospedes = serializers.IntegerField()
    banheiros = serializers.IntegerField()
    permite_animais = serializers.BooleanField()
    vlr_limpeza = serializers.FloatField()
    data_ativacao = serializers.DateField()

    class Meta:
        model = Imoveis
        fields = '__all__'

class AnunciosSerializers(serializers.ModelSerializer):
    id_anuncio = serializers.IntegerField()
    plataforma_anuncio = serializers.CharField()
    taxa_plataforma = serializers.FloatField()
    id_imovel = Imoveis()

    class Meta:
        model = Anuncios
        fields = '__all__'

class ReservasSerializers(serializers.ModelSerializer):
    id_anuncio = Anuncios()
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    vlr_total = serializers.FloatField()
    comentario = serializers.CharField()
    hospedes = serializers.IntegerField()

    class Meta:
        model = Reservas
        fields = '__all__'
