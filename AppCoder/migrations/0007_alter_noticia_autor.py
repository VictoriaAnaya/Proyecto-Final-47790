# Generated by Django 4.2.7 on 2023-12-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_remove_usuario_id_alter_usuario_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(max_length=100),
        ),
    ]
