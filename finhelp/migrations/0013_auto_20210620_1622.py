# Generated by Django 3.2.4 on 2021-06-20 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finhelp', '0012_auto_20210619_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ativo',
            old_name='description',
            new_name='desc_empresa',
        ),
        migrations.RenameField(
            model_name='ativo',
            old_name='company_name',
            new_name='nome_empresa',
        ),
        migrations.RenameField(
            model_name='histativo',
            old_name='perc_change',
            new_name='porcentagem',
        ),
        migrations.RenameField(
            model_name='histativo',
            old_name='last_hist',
            new_name='ultimo_hist',
        ),
        migrations.RenameField(
            model_name='histativo',
            old_name='val_ant',
            new_name='valor_anterior',
        ),
    ]
