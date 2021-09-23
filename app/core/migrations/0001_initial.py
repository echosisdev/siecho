# Generated by Django 3.2.7 on 2021-09-22 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('parentesco', models.CharField(max_length=255)),
                ('telefone1', models.CharField(max_length=255)),
                ('telefone2', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticoITS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('pre-tarv', 'pre-tarv'), ('tarv', 'tarv')], max_length=50)),
                ('numero', models.IntegerField()),
                ('pagina', models.IntegerField()),
                ('linha', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('genero', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=20)),
                ('data_nascimento', models.DateTimeField()),
                ('telefone', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=500, null=True)),
                ('confidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.confidente')),
                ('livro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.livro')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoLaboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TesteHivPos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_teste', models.CharField(choices=[('TR', 'TR'), ('PCRE', 'PCRE')], max_length=10)),
                ('data_teste', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeSanitaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.distrito')),
            ],
            options={
                'verbose_name': 'Unidade Sanitaria',
                'verbose_name_plural': 'Unidades Sanitarias',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_programa', models.CharField(choices=[('PRE-TARV', 'PRE-TARV'), ('TARV', 'TARV')], max_length=20)),
                ('data_inicio', models.DateTimeField()),
                ('formas_entrada', models.CharField(choices=[('transferido de', 'transferido de'), ('inscricao', 'inscricao')], max_length=50)),
                ('regime_arv', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_permanencia', models.CharField(choices=[('Activo', 'Activo'), ('Abandono', 'Abandono'), ('Transferido para', 'Transferido para'), ('Obito', 'Obito')], max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
                ('unidade_sanitaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria')),
            ],
        ),
        migrations.CreateModel(
            name='FichaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField()),
                ('data_proxima_consulta', models.DateTimeField()),
                ('populacao_chave', models.CharField(blank=True, max_length=100, null=True)),
                ('populacao_vulneravel', models.CharField(blank=True, max_length=100, null=True)),
                ('gravidez', models.BooleanField(default=False)),
                ('lactante', models.BooleanField(default=False)),
                ('data_ultima_menstruacao', models.DateTimeField(blank=True, null=True)),
                ('tensao_arterial', models.CharField(blank=True, max_length=100, null=True)),
                ('estadio_OMS', models.CharField(blank=True, max_length=100, null=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=2)),
                ('crianca_edemas', models.CharField(blank=True, max_length=100, null=True)),
                ('altura', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('imc', models.DecimalField(decimal_places=2, max_digits=2)),
                ('tem_sintomas_tb', models.CharField(blank=True, max_length=10, null=True)),
                ('diagnostico_tb_activo', models.CharField(blank=True, max_length=10, null=True)),
                ('profilaxia_inh', models.CharField(blank=True, max_length=10, null=True)),
                ('efeitos_secundarios_inh', models.CharField(blank=True, max_length=10, null=True)),
                ('profilaxia_ctz', models.CharField(blank=True, max_length=10, null=True)),
                ('efeitos_secundarios_ctz', models.CharField(blank=True, max_length=10, null=True)),
                ('tratamento_tb', models.CharField(blank=True, max_length=10, null=True)),
                ('data_tb', models.DateTimeField(blank=True, null=True)),
                ('sintomas_tb', models.CharField(blank=True, max_length=50, null=True)),
                ('tem_sintomas_its', models.CharField(blank=True, max_length=50, null=True)),
                ('infecoes_oportunistas', models.CharField(blank=True, max_length=155, null=True)),
                ('referencia_sector', models.CharField(blank=True, max_length=255, null=True)),
                ('elegivel_grupo_apoio', models.CharField(blank=True, max_length=255, null=True)),
                ('criancas_reveladas', models.CharField(blank=True, max_length=255, null=True)),
                ('pais_cuidadores', models.CharField(blank=True, max_length=255, null=True)),
                ('adolescentes_reveladas', models.CharField(blank=True, max_length=255, null=True)),
                ('mae_para_mae', models.CharField(blank=True, max_length=255, null=True)),
                ('elegivel_mdc', models.CharField(blank=True, max_length=255, null=True)),
                ('gaac', models.CharField(blank=True, max_length=255, null=True)),
                ('abordagem_familiar', models.CharField(blank=True, max_length=255, null=True)),
                ('clubes_adesao', models.CharField(blank=True, max_length=255, null=True)),
                ('paragem_unica', models.CharField(blank=True, max_length=255, null=True)),
                ('fluxo_rapido', models.CharField(blank=True, max_length=255, null=True)),
                ('dispensa_trimestral', models.CharField(blank=True, max_length=255, null=True)),
                ('dispensa_semestral', models.CharField(blank=True, max_length=255, null=True)),
                ('dispensa_comunitaria', models.CharField(blank=True, max_length=255, null=True)),
                ('farmacia_privada', models.CharField(blank=True, max_length=255, null=True)),
                ('diagnostico_its', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.diagnosticoits')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
        ),
        migrations.CreateModel(
            name='FichaResumo',
            fields=[
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.paciente')),
                ('data_abertura', models.DateTimeField()),
                ('data_teste_hiv_pos', models.DateTimeField(blank=True, null=True)),
                ('hepatite', models.BooleanField(default=False)),
                ('data_hepatite', models.DateTimeField(blank=True, null=True)),
                ('diabetes', models.BooleanField(default=False)),
                ('data_diabetes', models.DateTimeField(blank=True, null=True)),
                ('tb', models.BooleanField(default=False)),
                ('data_tb', models.DateTimeField(blank=True, null=True)),
                ('hta', models.BooleanField(default=False)),
                ('data_hta', models.DateTimeField(blank=True, null=True)),
                ('criptococose', models.BooleanField(default=False)),
                ('data_criptococose', models.DateTimeField(blank=True, null=True)),
                ('s_kapose', models.BooleanField(default=False)),
                ('data_kapose', models.DateTimeField(blank=True, null=True)),
                ('via_positivo', models.BooleanField(default=False)),
                ('data_via', models.DateTimeField(blank=True, null=True)),
                ('outra', models.CharField(blank=True, max_length=255, null=True)),
                ('data_outra', models.DateTimeField(blank=True, null=True)),
                ('ultimo_cd4', models.IntegerField()),
                ('data_cd4', models.DateTimeField(blank=True, null=True)),
                ('ultima_cv', models.IntegerField()),
                ('data_cv', models.DateTimeField(null=True)),
                ('ultima_ctz_data_inicio', models.DateTimeField(blank=True, null=True)),
                ('ultima_ctz_data_fim', models.DateTimeField(null=True)),
                ('gravidez', models.BooleanField(default=False)),
                ('lactante', models.BooleanField(default=False)),
                ('estadio_oms', models.CharField(blank=True, max_length=10, null=True)),
                ('teste_hiv_pos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.testehivpos')),
                ('unidade_sanitaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria')),
            ],
        ),
    ]
