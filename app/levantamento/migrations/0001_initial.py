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
            name='Filt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_levantamento', models.DateTimeField()),
                ('regime_tpt', models.CharField(max_length=100)),
                ('tipo_dispensa', models.CharField(max_length=100)),
                ('seguimento_tratamento', models.CharField(blank=True, max_length=100, null=True)),
                ('data_proximo_levantamento', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location')),
            ],
        ),
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_levantamento', models.DateTimeField()),
                ('regime', models.CharField(max_length=100)),
                ('formulacao', models.CharField(blank=True, max_length=100, null=True)),
                ('quantidade', models.IntegerField()),
                ('dosagem', models.CharField(max_length=100)),
                ('data_proximo_levantamento', models.DateTimeField()),
                ('lev_capmo_acomodacao', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_campo', models.IntegerField(blank=True, null=True)),
                ('modo_dispensa', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
    ]
