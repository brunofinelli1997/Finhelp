# Generated by Django 3.2.4 on 2021-06-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finhelp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='b3',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
