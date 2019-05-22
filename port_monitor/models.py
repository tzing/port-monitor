from django.db import models
from django.utils.translation import gettext_lazy as _

from . import settings


class MonitorTarget(models.Model):
    hostname = models.CharField(
        max_length=256,
        verbose_name=_('Hostname'),
    )

    port = models.IntegerField(
        default=settings.DEFAULT_PORT,
        verbose_name=_('Port'),
    )

    order = models.IntegerField(
        default=-1,
        verbose_name=_('Order'),
        help_text=_(
            'It will be shown in the upper position if the number is higher.'),
    )

    class Meta:
        verbose_name = _('Monitor target')
        verbose_name_plural = _('Monitor targets')

    def __str__(self):
        return f'{self.hostname} :{self.port}'
