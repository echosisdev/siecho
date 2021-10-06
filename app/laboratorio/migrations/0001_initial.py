# Generated by Django 3.2.7 on 2021-10-06 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExameClinico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField()),
                ('data_colheita', models.DateTimeField()),
                ('data_resultado', models.DateTimeField()),
                ('globulos_brancos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('globulos_vermelhos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hemoglobina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hematorcito', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vol_corpuscular_med', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('conc_media_hemoglob_corp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('plaquetas', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('larg_distr_gv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('velc_sedime_gv', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vol_medio_plaquetas', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tipagem_sanguinea', models.CharField(blank=True, max_length=255, null=True)),
                ('linfocitos_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('linfocitos_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('neutrofilos_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('neutrofilos_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eosinofilo_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eosinofilo_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('basofio_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('basofio_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monocito_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monocito_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('teste_vdr', models.CharField(blank=True, max_length=50, null=True)),
                ('rpr', models.CharField(blank=True, max_length=50, null=True)),
                ('cd4_abs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cd4_perc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('geneexpert', models.CharField(blank=True, max_length=50, null=True)),
                ('xpert_mtb', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_mtb_detetado', models.CharField(blank=True, max_length=50, null=True)),
                ('resistencia_rifampin', models.CharField(blank=True, max_length=50, null=True)),
                ('cultura', models.CharField(blank=True, max_length=50, null=True)),
                ('tb_lam', models.CharField(blank=True, max_length=50, null=True)),
                ('carga_viral', models.CharField(blank=True, max_length=50, null=True)),
                ('baciloscopial', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_positividade', models.CharField(blank=True, max_length=50)),
                ('albumina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('asparato_aminotransferiase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alanina_aminotransferiase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amilase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('birrubina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('birrubina_direita', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('colesterol_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hdl_colesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ldl_colesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('creatina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('creatina_quinase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fosfatase_alcalina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gama_glutamil', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('glucose', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lactato_desidrogenase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lactato', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lipase', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_proteina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('triglicerides', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ureia', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cloreto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('potassio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sodio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('globulinas', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pcr', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
            options={
                'verbose_name': 'Exame Clinico',
                'verbose_name_plural': 'Exames Clinicos',
            },
        ),
    ]
