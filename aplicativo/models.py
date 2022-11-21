from django.db import models
from django.db.models import FloatField
from django.db import IntegrityError
# Create your models here.

class Imoveis(models.Model):
    id = models.BigIntegerField(primary_key=True)
    limite_hospedes = models.BigIntegerField(blank=True, null=True)
    banheiros = models.BigIntegerField(blank=True, null=True)
    permite_animais = models.BooleanField(blank=True, null=True)
    vlr_limpeza = models.FloatField(blank=True, null=True)
    data_ativacao = models.DateField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Anuncios(models.Model):
    id_anuncio = models.BigIntegerField(primary_key=True)
    plataforma_anuncio = models.CharField(max_length=100, blank=True, null=True)
    taxa_plataforma = models.FloatField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True ,blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id_imovel = models.ForeignKey('Imoveis', models.CASCADE, db_column='id_imovel', blank=True, null=True)




class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_anuncio = models.ForeignKey('Anuncios', models.CASCADE, db_column='id_anuncio', blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    vlr_total = models.FloatField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    hospedes = models.BigIntegerField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)


    def save(self, *args, **kwargs):
            if self.check_in >= self.check_out:
                raise IntegrityError    
            super(Reservas, self).save(*args, **kwargs)