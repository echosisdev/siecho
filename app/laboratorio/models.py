from django.db import models
from core.models import Paciente, UnidadeSanitaria



class ExameClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now=False) 
    data_colheita = models.DateTimeField(auto_now=False)
    data_resultado = models.DateTimeField(auto_now=False)
    globulos_brancos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    globulos_vermelhos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hemoglobina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hematorcito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vol_corpuscular_med = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    conc_media_hemoglob_corp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    plaquetas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    larg_distr_gv = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    velc_sedime_gv = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vol_medio_plaquetas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tipagem_sanguinea = models.CharField(max_length=255, null=True, blank=True)
    linfocitos_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    linfocitos_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    neutrofilos_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    neutrofilos_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eosinofilo_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eosinofilo_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    basofio_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    basofio_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monocito_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monocito_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    teste_vdr = models.CharField(max_length=50, blank=True, null=True)
    rpr = models.CharField(max_length=50, blank=True, null=True)
    cd4_abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cd4_perc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carga_viral = models.IntegerField()
    geneexpert = models.CharField(max_length=50, blank=True, null=True)
    xpert_mtb = models.CharField(max_length=50, blank=True, null=True)
    nivel_mtb_detetado = models.CharField(max_length=50, blank=True, null=True)
    resistencia_rifampin = models.CharField(max_length=50, blank=True, null=True)
    cultura = models.CharField(max_length=50, blank=True, null=True)
    tb_lam = models.CharField(max_length=50, blank=True, null=True)
    carga_viral = models.CharField(max_length=50, blank=True, null=True)
    baciloscopial = models.CharField(max_length=50, blank=True, null=True)
    nivel_positividade = models.CharField(max_length=50, blank=True)
    albumina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    asparato_aminotransferiase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    alanina_aminotransferiase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amilase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    birrubina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    birrubina_direita = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    colesterol_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hdl_colesterol = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ldl_colesterol = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    creatina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    creatina_quinase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fosfatase_alcalina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gama_glutamil = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    glucose = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lactato_desidrogenase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lactato = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lipase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_proteina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    triglicerides = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ureia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cloreto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    potassio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sodio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    globulinas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pcr = models.CharField(max_length=50, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    unidade_sanitaria = models.ForeignKey(UnidadeSanitaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.paciente.nome