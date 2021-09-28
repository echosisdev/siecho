from django.contrib import admin
from core.models import Location, Paciente, Programa, FichaResumo, FichaClinica, TesteHivPos, Confidente
from apss.models import FichaApss, VisitaDomiciliaria, RelatorioVisita
from laboratorio.models import ExameClinico

classes = [
    Location,
    Paciente,
    Programa,
    FichaResumo,
    FichaClinica,
    TesteHivPos,
    Confidente,
    FichaApss,
    VisitaDomiciliaria,
    RelatorioVisita,
    ExameClinico
]

for model in classes:
    admin.site.register(model)
    
    