# Generated by Django 5.2.1 on 2025-07-02 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_autualizado_em_produtos_atualizado_em'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='home.categoriaproduto')),
            ],
        ),
    ]
