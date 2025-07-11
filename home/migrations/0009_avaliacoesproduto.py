# Generated by Django 5.2.1 on 2025-07-08 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_carrinho'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacoesProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], decimal_places=1, max_digits=2)),
                ('comentario', models.TextField()),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='home.produtos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minhas_avaliacoes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
