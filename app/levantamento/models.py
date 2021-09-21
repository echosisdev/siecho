from django.db import models
from core.models import Paciente, UnidadeSanitaria

class Fila(models.Model):
    data_levantamento = models.DateTimeField(auto_now=False)
    regime = models.CharField(max_length=100)
    formulacao = models.CharField(max_length=100, blank=True, null=True)
    quantidade = models.IntegerField()
    dosagem = models.CharField(max_length=100)
    data_proximo_levantamento = models.DateTimeField()
    lev_capmo_acomodacao = models.CharField(max_length=100, blank=True, null=True)
    numero_campo = models.IntegerField(null=True, blank=True)
    modo_dispensa = models.CharField(max_length=100, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    unidade_sanitaria = models.ForeignKey(UnidadeSanitaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.paciente.nome
    
class Filt(models.Model):
    data_levantamento = models.DateTimeField(auto_now=False)
    regime_tpt = models.CharField(max_length=100)
    tipo_dispensa = models.CharField(max_length=100)
    seguimento_tratamento = models.CharField(max_length=100, blank=True, null=True)
    data_proximo_levantamento = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.regime_tpt
    
