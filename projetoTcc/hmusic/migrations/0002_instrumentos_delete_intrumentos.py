# Generated by Django 4.2.5 on 2023-09-21 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hmusic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_instrumentos')),
                ('descricao', models.TextField(max_length=1000)),
                ('categoria', models.CharField(choices=[('CORDAS', 'Cordas'), ('SOPRO', 'Sopro'), ('ACESSORIOS', 'Acessorios')], max_length=15)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Intrumentos',
        ),
    ]
