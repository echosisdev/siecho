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
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=20, choices=GENERO)
    data_nascimento = models.DateTimeField(auto_now=False)
    nid = models.CharField(max_length=255)
    telefone = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, blank=True, null=True)
    confidente = models.ForeignKey(Confidente, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nome

class TesteHivPos(models.Model):
    tipo_teste = models.CharField(max_length=10, choices=TESTE_HIV)
    data_teste = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.nome
    

    
class FichaResumo(models.Model):
    data_abertura = models.DateTimeField(auto_now=False)
    teste_hiv_pos = models.CharField(max_length=10, choices=TESTE_HIV)
    teste_hiv_pos = models.ForeignKey(TesteHivPos, on_delete=models.CASCADE)
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
    