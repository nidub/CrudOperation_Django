# Generated by Django 3.2.8 on 2021-10-23 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='core',
            options={'ordering': ['-published']},
        ),
    ]
