# Generated by Django 5.0.1 on 2024-01-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]