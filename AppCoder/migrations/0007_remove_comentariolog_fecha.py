# Generated by Django 4.1.5 on 2023-02-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_comentariolog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentariolog',
            name='fecha',
        ),
    ]
