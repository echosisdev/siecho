# Generated by Django 3.2.7 on 2021-09-21 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitaDomiciliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro_chamadas', models.IntegerField(blank=True, null=True)),
                ('pagina_livro', models.IntegerField(blank=True, null=True)),
                ('linha_livro', models.IntegerField(blank=True, null=True)),
                ('nome_casa', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(blank=True, max_length=255, null=True)),
                ('avenida_ou_rua', models.CharField(blank=True, max_length=255, null=True)),
                ('aldeia_comunidade', models.CharField(blank=True, max_length=255, null=True)),
                ('quarteirao', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_casa', models.CharField(blank=True, max_length=255, null=True)),
                ('contacto_paciente', models.CharField(blank=True, max_length=255, null=True)),
                ('ponto_referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('paciente_autorizou', models.CharField(blank=True, max_length=255, null=True)),
                ('nome_confidente', models.CharField(blank=True, max_length=255, null=True)),
                ('crianca_exposta', models.CharField(blank=True, max_length=255, null=True)),
                ('bk', models.CharField(blank=True, max_length=255, null=True)),
                ('tb_sem_tratamento', models.CharField(blank=True, max_length=255, null=True)),
                ('sem_cv', models.CharField(blank=True, max_length=255, null=True)),
                ('falencia_terapeutica', models.CharField(blank=True, max_length=255, null=True)),
                ('elegivel_tarv', models.CharField(blank=True, max_length=255, null=True)),
                ('faltoso_farmacia', models.CharField(blank=True, max_length=255, null=True)),
                ('faltoso_consultas', models.CharField(blank=True, max_length=255, null=True)),
                ('cv_elevada', models.CharField(blank=True, max_length=255, null=True)),
                ('seguimento_preventivo', models.CharField(blank=True, max_length=255, null=True)),
                ('outro', models.CharField(blank=True, max_length=255, null=True)),
                ('servico_refere', models.CharField(max_length=255, null=True)),
                ('voluntario', models.CharField(blank=True, max_length=255, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
                ('unidade_sanitaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria')),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_visita', models.CharField(max_length=100)),
                ('data_visita', models.DateTimeField()),
                ('motivo_falta', models.CharField(blank=True, max_length=100, null=True)),
                ('relatorio_visita', models.CharField(blank=True, max_length=100, null=True)),
                ('paciente_encaminhado_para', models.CharField(blank=True, max_length=100, null=True)),
                ('data_para_retorno', models.DateTimeField(blank=True, null=True)),
                ('motivo_nao_encontrado', models.CharField(blank=True, max_length=100, null=True)),
                ('info_dada_por', models.CharField(blank=True, max_length=100, null=True)),
                ('contacto_informante', models.CharField(blank=True, max_length=100, null=True)),
                ('data_devolucao_cartao', models.CharField(blank=True, max_length=100, null=True)),
                ('pessoa_efectuou_visita', models.CharField(max_length=100)),
                ('visita_domiciliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apss.visitadomiciliaria')),
            ],
        ),
        migrations.CreateModel(
            name='FichaApss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('populacao_chave', models.CharField(blank=True, max_length=100, null=True)),
                ('livro_apps', models.IntegerField()),
                ('pagina_livro', models.IntegerField()),
                ('linha_livro', models.IntegerField()),
                ('consulta_actual', models.DateTimeField()),
                ('proxima_consulta', models.DateTimeField()),
                ('estado_revelacao_cr_adol', models.CharField(blank=True, max_length=100, null=True)),
                ('educ_sobre_hiv', models.CharField(blank=True, max_length=100, null=True)),
                ('recusa_resultado_pos', models.BooleanField(blank=True, default=False, null=True)),
                ('sente_doent_demais', models.BooleanField(blank=True, default=False, null=True)),
                ('nao_acredita_tarv', models.BooleanField(blank=True, default=False, null=True)),
                ('muitos_comprimidos', models.BooleanField(blank=True, default=False, null=True)),
                ('falta_alimentacao', models.BooleanField(blank=True, default=False, null=True)),
                ('falta_apoio_familiar', models.BooleanField(blank=True, default=False, null=True)),
                ('ansiedade', models.BooleanField(blank=True, default=False, null=True)),
                ('difcdad_revelar_parceiro', models.BooleanField(blank=True, default=False, null=True)),
                ('toxicidade', models.BooleanField(blank=True, default=False, null=True)),
                ('perdeu_comprimidos', models.BooleanField(blank=True, default=False, null=True)),
                ('estigma_ou_descriminacao', models.BooleanField(blank=True, default=False, null=True)),
                ('problemas_transp', models.BooleanField(blank=True, default=False, null=True)),
                ('vbg', models.BooleanField(blank=True, default=False, null=True)),
                ('uso_alcool_drogas', models.BooleanField(blank=True, default=False, null=True)),
                ('outro', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo_seguro', models.CharField(blank=True, max_length=100, null=True)),
                ('revelacao_seroestado_parceiro', models.CharField(blank=True, max_length=100, null=True)),
                ('importancia_adesao_tarv', models.CharField(blank=True, max_length=100, null=True)),
                ('inf_transmissao_sexual', models.CharField(blank=True, max_length=100, null=True)),
                ('pf_gs_ptv', models.CharField(blank=True, max_length=100, null=True)),
                ('necess_apoio_comunitario', models.CharField(blank=True, max_length=100, null=True)),
                ('oferta_lubrificantes', models.CharField(blank=True, max_length=100, null=True)),
                ('informou_seroestado', models.CharField(blank=True, max_length=100, null=True)),
                ('parentesco', models.CharField(blank=True, max_length=100, null=True)),
                ('quem_administra_arv', models.CharField(blank=True, max_length=100, null=True)),
                ('parentesco_administra', models.CharField(blank=True, max_length=100, null=True)),
                ('horario_esq_dose_viagem', models.CharField(blank=True, max_length=100, null=True)),
                ('efeitos_secundarios', models.CharField(blank=True, max_length=100, null=True)),
                ('adesao_tarv', models.CharField(blank=True, max_length=100, null=True)),
                ('motivo_consulta', models.CharField(blank=True, max_length=100, null=True)),
                ('cr_revelada', models.CharField(blank=True, max_length=100, null=True)),
                ('adolescente_revelado', models.CharField(blank=True, max_length=100, null=True)),
                ('pais_cuidadores', models.CharField(blank=True, max_length=100, null=True)),
                ('mae_para_mae', models.CharField(blank=True, max_length=100, null=True)),
                ('gaac', models.CharField(blank=True, max_length=100, null=True)),
                ('fluxo_rapido', models.CharField(blank=True, max_length=100, null=True)),
                ('dispensa_trimestral', models.CharField(blank=True, max_length=100, null=True)),
                ('dispensa_comunitaria', models.CharField(blank=True, max_length=100, null=True)),
                ('dispensa_semestral', models.CharField(blank=True, max_length=100, null=True)),
                ('concorda_ser_contactado', models.CharField(blank=True, max_length=100, null=True)),
                ('data_consentimento', models.DateTimeField(blank=True, null=True)),
                ('tipo_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('confidente_concorda_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
                ('unidade_sanitaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria')),
            ],
        ),
    ]
