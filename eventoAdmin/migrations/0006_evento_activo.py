# Generated by Django 4.2.7 on 2023-11-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventoAdmin', '0005_alter_evento_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
