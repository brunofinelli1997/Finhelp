# Generated by Django 3.2.4 on 2021-06-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finhelp', '0003_ativo_fk_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ativo',
            old_name='name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='ativo',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
