# Generated by Django 3.2 on 2021-05-03 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_alter_consulta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['dia', 'horario']},
        ),
    ]
