from django.contrib import admin
from core.models import Location, Paciente, Programa, Inscricao, ConsultaClinica, TesteHivPos
from apss.models import ConsultaApss, VisitaDomiciliaria, RelatorioVisita
from laboratorio.models import ExameClinico

classes = [
    Location,
    Paciente,
    Programa,
    Inscricao,
    ConsultaClinica,
    TesteHivPos,
    ConsultaApss,
    VisitaDomiciliaria,
    RelatorioVisita,
    ExameClinico
]

for model in classes:
    admin.site.register(model)
    
    