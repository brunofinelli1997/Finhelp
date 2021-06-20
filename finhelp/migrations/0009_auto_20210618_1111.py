# Generated by Django 3.2.4 on 2021-06-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finhelp', '0008_remove_valativo_fk_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='data_atualizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ativo',
            name='perc_change',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ativo',
            name='val_ant',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ativo',
            name='valor',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='ValAtivo',
        ),
    ]