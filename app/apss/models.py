from django.db import models
from core.models import Paciente, Location

class ConsultaApss(models.Model):
    populacao_chave = models.CharField(max_length=100, blank=True, null=True)
    livro_apps = models.IntegerField()
    pagina_livro = models.IntegerField()
    linha_livro = models.IntegerField()
    consulta_actual = models.DateTimeField(auto_now=False)
    proxima_consulta = models.DateTimeField(auto_now=False)
    estado_revelacao_cr_adol = models.CharField(max_length=100, blank=True, null=True)
    educ_sobre_hiv = models.CharField(max_length=100, blank=True, null=True)
    recusa_resultado_pos = models.BooleanField(default=False, null=True, blank=True)
    sente_doent_demais = models.BooleanField(default=False, null=True, blank=True)
    nao_acredita_tarv = models.BooleanField(default=False, null=True, blank=True)
    muitos_comprimidos = models.BooleanField(default=False, null=True, blank=True)
    falta_alimentacao = models.BooleanField(default=False, null=True, blank=True)
    falta_apoio_familiar = models.BooleanField(default=False, null=True, blank=True)
    ansiedade = models.BooleanField(default=False, null=True, blank=True)
    difcdad_revelar_parceiro = models.BooleanField(default=False, null=True, blank=True)
    toxicidade = models.BooleanField(default=False, null=True, blank=True)
    perdeu_comprimidos = models.BooleanField(default=False, null=True, blank=True)
    estigma_ou_descriminacao = models.BooleanField(default=False, null=True, blank=True)
    problemas_transp = models.BooleanField(default=False, null=True, blank=True)
    vbg = models.BooleanField(default=False, null=True, blank=True)
    uso_alcool_drogas = models.BooleanField(default=False, null=True, blank=True)
    outro = models.CharField(max_length=100, null=True, blank=True)
    sexo_seguro = models.CharField(max_length=100, null=True, blank=True)
    revelacao_seroestado_parceiro = models.CharField(max_length=100, null=True, blank=True)
    importancia_adesao_tarv = models.CharField(max_length=100, null=True, blank=True)
    inf_transmissao_sexual = models.CharField(max_length=100, null=True, blank=True)
    pf_gs_ptv = models.CharField(max_length=100, null=True, blank=True)
    necess_apoio_comunitario = models.CharField(max_length=100, null=True, blank=True)
    oferta_lubrificantes = models.CharField(max_length=100, null=True, blank=True)
    informou_seroestado = models.CharField(max_length=100, null=True, blank=True)
    parentesco = models.CharField(max_length=100, null=True, blank=True)
    quem_administra_arv = models.CharField(max_length=100, null=True, blank=True)
    parentesco_administra = models.CharField(max_length=100, null=True, blank=True)
    horario_esq_dose_viagem = models.CharField(max_length=100, null=True, blank=True)
    efeitos_secundarios = models.CharField(max_length=100, null=True, blank=True)
    adesao_tarv = models.CharField(max_length=100, null=True, blank=True)
    motivo_consulta = models.CharField(max_length=100, null=True, blank=True)
    cr_revelada = models.CharField(max_length=100, null=True, blank=True)
    adolescente_revelado = models.CharField(max_length=100, null=True, blank=True)
    pais_cuidadores = models.CharField(max_length=100, null=True, blank=True)
    mae_para_mae = models.CharField(max_length=100, null=True, blank=True)
    gaac = models.CharField(max_length=100, null=True, blank=True)
    fluxo_rapido = models.CharField(max_length=100, null=True, blank=True)
    dispensa_trimestral = models.CharField(max_length=100, null=True, blank=True)
    dispensa_comunitaria = models.CharField(max_length=100, null=True, blank=True)
    dispensa_semestral = models.CharField(max_length=100, null=True, blank=True)
    concorda_ser_contactado = models.CharField(max_length=100, null=True, blank=True)
    data_consentimento = models.DateTimeField(auto_now=False, null=True, blank=True)
    tipo_contacto = models.CharField(max_length=100, null=True, blank=True)
    confidente_concorda_contacto = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Consulta Apss'
        verbose_name_plural = 'Consultas Apss'


    def __str__(self):
        return self.paciente.nome
    
class VisitaDomiciliaria(models.Model):
    livro_chamadas = models.IntegerField(null=True, blank=True)
    pagina_livro = models.IntegerField(null=True, blank=True)
    linha_livro = models.IntegerField(null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome_casa = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    avenida_ou_rua = models.CharField(max_length=255, null=True, blank=True)
    aldeia_comunidade = models.CharField(max_length=255, null=True, blank=True)
    quarteirao = models.CharField(max_length=255, null=True, blank=True)
    numero_casa = models.CharField(max_length=255, null=True, blank=True)
    contacto_paciente = models.CharField(max_length=255, null=True, blank=True)
    ponto_referencia = models.CharField(max_length=255, null=True, blank=True)
    paciente_autorizou = models.CharField(max_length=255, null=True, blank=True)
    nome_confidente = models.CharField(max_length=255, null=True, blank=True)
    crianca_exposta = models.CharField(max_length=255, null=True, blank=True)
    bk = models.CharField(max_length=255, null=True, blank=True)
    tb_sem_tratamento = models.CharField(max_length=255, null=True, blank=True)
    sem_cv = models.CharField(max_length=255, null=True, blank=True)
    falencia_terapeutica = models.CharField(max_length=255, null=True, blank=True)
    elegivel_tarv = models.CharField(max_length=255, null=True, blank=True)
    faltoso_farmacia = models.CharField(max_length=255, null=True, blank=True)
    faltoso_consultas = models.CharField(max_length=255, null=True, blank=True)
    cv_elevada = models.CharField(max_length=255, null=True, blank=True)
    seguimento_preventivo = models.CharField(max_length=255, null=True, blank=True)
    outro = models.CharField(max_length=255, null=True, blank=True)
    servico_refere = models.CharField(max_length=255, null=True)
    voluntario = models.CharField(max_length=255, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.paciente.nome
    
class RelatorioVisita(models.Model):
    tipo_visita = models.CharField(max_length=100)
    data_visita = models.DateTimeField(auto_now=False)
    motivo_falta = models.CharField(max_length=100, null=True, blank=True)
    relatorio_visita = models.CharField(max_length=100, null=True, blank=True)
    paciente_encaminhado_para = models.CharField(max_length=100, null=True, blank=True)
    data_para_retorno = models.DateTimeField(auto_now=False, null=True, blank=True)
    motivo_nao_encontrado = models.CharField(max_length=100, null=True, blank=True)
    info_dada_por = models.CharField(max_length=100, null=True, blank=True)
    contacto_informante = models.CharField(max_length=100, null=True, blank=True)
    data_devolucao_cartao = models.CharField(max_length=100, null=True, blank=True)
    pessoa_efectuou_visita = models.CharField(max_length=100)
    visita_domiciliaria = models.ForeignKey(VisitaDomiciliaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo_visita
    