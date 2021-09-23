from django.db import models

TIPO_LIVRO = (
    ('pre-tarv', 'pre-tarv'),
    ('tarv', 'tarv'),
)

GENERO = (
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino'),
)

TESTE_HIV = (
    ('TR', 'TR'),
    ('PCRE', 'PCRE'),
)

TIPO_PROGRAMA= (
    ('PRE-TARV', 'PRE-TARV'),
    ('TARV', 'TARV'),
)

FORMAS_ENTRADA = (
    ('transferido de', 'transferido de'),
    ('inscricao', 'inscricao'),
)

ESTADO_PERMANENCIA = (
    ('Activo', 'Activo'),
    ('Abandono', 'Abandono'),
    ('Transferido para', 'Transferido para'),
    ('Obito', 'Obito'),
)
# Create your models here.
class Provincia(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Distrito(models.Model):
    """Model definition for Distrito."""
    nome = models.CharField(max_length=255)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class UnidadeSanitaria(models.Model):
    nome = models.CharField(max_length=255)
    distrito = models.ForeignKey('Distrito', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Unidade Sanitaria'
        verbose_name_plural = 'Unidades Sanitarias'
    
    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    tipo = models.CharField(max_length=50, choices=TIPO_LIVRO)
    numero = models.IntegerField()
    pagina = models.IntegerField()
    linha = models.IntegerField()
    
    def __str__(self):
        return self.tipo
    
class Confidente(models.Model):
    nome = models.CharField(max_length=255)
    parentesco = models.CharField(max_length=255)
    telefone1 = models.CharField(max_length=255)
    telefone2 = models.CharField(max_length=255)
    endereco = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.nome
        
class Paciente(models.Model):
    nid = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=20, choices=GENERO)
    data_nascimento = models.DateTimeField(auto_now=False)
    telefone = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)
    confidente = models.ForeignKey(Confidente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.nome

class TesteHivPos(models.Model):
    tipo_teste = models.CharField(max_length=10, choices=TESTE_HIV)
    data_teste = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.tipo_teste
    

    
class FichaResumo(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    data_abertura = models.DateTimeField(auto_now=False)
    data_teste_hiv_pos = models.DateTimeField(auto_now=False, blank=True, null=True)
    teste_hiv_pos = models.ForeignKey(TesteHivPos, on_delete=models.CASCADE, blank=True, null=True)
    hepatite = models.BooleanField(default=False)
    data_hepatite = models.DateTimeField(auto_now=False, null=True, blank=True)
    diabetes = models.BooleanField(default=False)
    data_diabetes = models.DateTimeField(auto_now=False, null=True, blank=True)
    tb = models.BooleanField(default=False)
    data_tb = models.DateTimeField(auto_now=False, null=True, blank=True)
    hta = models.BooleanField(default=False)
    data_hta = models.DateTimeField(auto_now=False, null=True, blank=True)
    criptococose = models.BooleanField(default=False)
    data_criptococose = models.DateTimeField(auto_now=False, null=True, blank=True)
    s_kapose = models.BooleanField(default=False)
    data_kapose = models.DateTimeField(auto_now=False, null=True, blank=True)
    via_positivo = models.BooleanField(default=False)
    data_via = models.DateTimeField(auto_now=False, null=True, blank=True)
    outra = models.CharField(max_length=255, null=True, blank=True)
    data_outra = models.DateTimeField(auto_now=False, null=True, blank=True)
    ultimo_cd4 = models.IntegerField()
    data_cd4 = models.DateTimeField(auto_now=False, null=True, blank=True)
    ultima_cv = models.IntegerField()
    data_cv = models.DateTimeField(auto_now=False, null=True)
    ultima_ctz_data_inicio = models.DateTimeField(auto_now=False, null=True, blank=True)
    ultima_ctz_data_fim = models.DateTimeField(auto_now=False, null=True)
    gravidez = models.BooleanField(default=False)
    lactante = models.BooleanField(default=False)
    estadio_oms = models.CharField(max_length=10, null=True, blank=True)
    unidade_sanitaria = models.ForeignKey(UnidadeSanitaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Programa(models.Model):
    tipo_programa = models.CharField(max_length=20, choices=TIPO_PROGRAMA)
    data_inicio = models.DateTimeField(auto_now=False)
    formas_entrada = models.CharField(max_length=50, choices=FORMAS_ENTRADA)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    regime_arv = models.CharField(max_length=100, null=True, blank=True)
    unidade_sanitaria = models.ForeignKey(UnidadeSanitaria, on_delete=models.CASCADE)
    estado_permanencia = models.CharField(max_length=100, choices=ESTADO_PERMANENCIA)

    def __str__(self):
        return self.tipo_programa

class DiagnosticoITS(models.Model):
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descricao

class ItemPedido(models.Model):
    pass
class PedidoLaboratorio(models.Model):
    pass
    
class FichaClinica(models.Model):
    data_consulta = models.DateTimeField(auto_now=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_proxima_consulta = models.DateTimeField(auto_now=False)
    populacao_chave = models.CharField(max_length=100, blank=True, null=True)
    populacao_vulneravel = models.CharField(max_length=100, blank=True, null=True)
    gravidez = models.BooleanField(default=False)
    lactante = models.BooleanField(default=False)
    data_ultima_menstruacao = models.DateTimeField(auto_now=False, null=True, blank=True)
    tensao_arterial = models.CharField(max_length=100, blank=True, null=True)
    estadio_OMS = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(decimal_places=2, max_digits=2)
    crianca_edemas = models.CharField(max_length=100, blank=True, null=True)
    altura = models.DecimalField(decimal_places=2, max_digits=2, null=True, blank=True)
    imc = models.DecimalField(decimal_places=2, max_digits=2)
    tem_sintomas_tb = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_tb_activo = models.CharField(max_length=10, blank=True, null=True)
    profilaxia_inh = models.CharField(max_length=10, blank=True, null=True)
    efeitos_secundarios_inh = models.CharField(max_length=10, blank=True, null=True)
    profilaxia_ctz = models.CharField(max_length=10, blank=True, null=True)
    efeitos_secundarios_ctz = models.CharField(max_length=10, blank=True, null=True)
    tratamento_tb = models.CharField(max_length=10, blank=True, null=True)
    data_tb = models.DateTimeField(auto_now=False, null=True, blank=True)
    sintomas_tb = models.CharField(max_length=50, blank=True, null=True)
    tem_sintomas_its = models.CharField(max_length=50, blank=True, null=True)
    diagnostico_its = models.ForeignKey(DiagnosticoITS, on_delete=models.SET_NULL, null=True)
    infecoes_oportunistas = models.CharField(max_length=155, blank=True, null=True)
    referencia_sector = models.CharField(max_length=255, blank=True, null=True)
    elegivel_grupo_apoio = models.CharField(max_length=255, blank=True, null=True)
    criancas_reveladas = models.CharField(max_length=255, blank=True, null=True)
    pais_cuidadores = models.CharField(max_length=255, blank=True, null=True)
    adolescentes_reveladas = models.CharField(max_length=255, blank=True, null=True)
    mae_para_mae = models.CharField(max_length=255, blank=True, null=True)
    elegivel_mdc = models.CharField(max_length=255, blank=True, null=True)
    gaac = models.CharField(max_length=255, blank=True, null=True)
    abordagem_familiar = models.CharField(max_length=255, blank=True, null=True)
    clubes_adesao = models.CharField(max_length=255, blank=True, null=True)
    paragem_unica = models.CharField(max_length=255, blank=True, null=True)
    fluxo_rapido = models.CharField(max_length=255, blank=True, null=True)
    dispensa_trimestral = models.CharField(max_length=255, blank=True, null=True)  
    dispensa_semestral = models.CharField(max_length=255, blank=True, null=True)
    dispensa_comunitaria = models.CharField(max_length=255, blank=True, null=True)
    farmacia_privada = models.CharField(max_length=255, blank=True, null=True)
    
    
