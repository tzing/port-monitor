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
