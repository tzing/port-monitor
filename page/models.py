from django.db import models
from django.utils.translation import gettext_lazy as _


class MonitorTarget(models.Model):
    hostname = models.CharField(max_length=256)
    port = models.IntegerField(default=80)

    class Meta:
        verbose_name = _('Monitor target')
        verbose_name_plural = _('Monitor targets')

    def __str__(self):
        return f'{self.hostname} :{self.port}'


class Setting(models.Model):
    query_interval = models.FloatField(
        verbose_name=_('Query interval'),
        help_text=_(
            'Fire a query every N second to check if addresses are still alive'
        ),
        default=300)

    def __str__(self):
        return 'Settings (only)'

    def save(self, *args, **kwargs):
        if Setting.objects.exists() and not self.pk:
            raise ValidationError('There is can be only one Setting instance')
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')
