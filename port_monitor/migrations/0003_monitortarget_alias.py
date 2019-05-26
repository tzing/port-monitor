# Generated by Django 2.2.1 on 2019-05-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_monitor', '0002_auto_20190522_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitortarget',
            name='alias',
            field=models.CharField(blank=True, help_text='A recognizable name to be displayed on info card.', max_length=256, null=True, verbose_name='Alias'),
        ),
    ]