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

    
class Location(models.Model):
    location_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    parent_location = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Paciente(models.Model):
    patient_id = models.CharField(max_length=255, primary_key=True)
    nid = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=20, choices=GENERO)
    data_nascimento = models.DateTimeField(auto_now=False)
    telefone = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    livro = models.CharField(max_length=15)
    pagina = models.CharField(max_length=4)
    linha = models.CharField(max_length=4)
    nome_confidente = models.CharField(max_length=255, blank=True, null=True)
    confidente_parentesco = models.CharField(max_length=255, blank=True, null=True)
    telefone1_confidente = models.CharField(max_length=255, blank=True, null=True)
    telefone2_confidente = models.CharField(max_length=255, blank=True, null=True)
    endereco_confidente = models.CharField(max_length=500, null=True, blank=True)
    distrito = models.CharField(max_length=100, null=True, blank=True)
    posto_administrativo = models.CharField(max_length=100, null=True, blank=True)
    localidade = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    ponto_referencia = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class TesteHivPos(models.Model):
    tipo_teste = models.CharField(max_length=10, choices=TESTE_HIV)
    data_teste = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.tipo_teste
    

    
class Inscricao(models.Model):
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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural = 'Inscricoes'
    
    def __str__(self):
        return self.nome
    
class Programa(models.Model):
    tipo_programa = models.CharField(max_length=20, choices=TIPO_PROGRAMA)
    data_inicio = models.DateTimeField(auto_now=False)
    formas_entrada = models.CharField(max_length=50, choices=FORMAS_ENTRADA)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    regime_arv = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    estado_permanencia = models.CharField(max_length=100, choices=ESTADO_PERMANENCIA)

    def __str__(self):
        return self.tipo_programa

class DiagnosticoITS(models.Model):
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descricao

class ConsultaClinica(models.Model):
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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Consulta Clinica'
        verbose_name_plural = 'Consultas Clinicas'
    
    def __str__(self):
        return self.paciente.nome
