# Generated by Django 3.2.4 on 2021-06-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lim_inf', models.FloatField()),
                ('lim_sup', models.FloatField()),
            ],
        ),
    ]
