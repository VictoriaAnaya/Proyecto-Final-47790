# Generated by Django 4.2.7 on 2023-12-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_remove_noticia_id_alter_noticia_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais_origen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
