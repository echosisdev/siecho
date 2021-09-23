from django.contrib import admin
from core.models import *
from apss.models import FichaApss, VisitaDomiciliaria, RelatorioVisita
from laboratorio.models import ExameClinico

classes = [
    Provincia,
    Distrito,
    UnidadeSanitaria,
    Paciente,
    Programa,
    FichaResumo,
    FichaClinica,
    Livro,
    TesteHivPos,
    Confidente,
    FichaApss,
    VisitaDomiciliaria,
    RelatorioVisita,
    ExameClinico
]

for model in classes:
    admin.site.register(model)
    
    