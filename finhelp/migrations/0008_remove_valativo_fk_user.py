# Generated by Django 3.2.4 on 2021-06-18 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finhelp', '0007_alter_valativo_fk_b3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valativo',
            name='fk_user',
        ),
    ]
