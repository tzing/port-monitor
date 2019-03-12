# Generated by Django 2.1.7 on 2019-03-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=256)),
                ('port', models.IntegerField(default=80)),
            ],
            options={
                'verbose_name': 'Monitor target',
                'verbose_name_plural': 'Monitor targets',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_interval', models.FloatField(default=300, help_text='Fire a query every N second to check if addresses are still alive', verbose_name='Query interval')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]