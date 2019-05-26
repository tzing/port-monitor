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

    alias = models.CharField(
        max_length=256,
        verbose_name=_('Alias'),
        null=True,
        blank=True,
        help_text=_('A recognizable name to be displayed on info card.'),
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
        if self.alias:
            return f'{self.hostname} :{self.port} ({self.alias})'
        return f'{self.hostname} :{self.port}'

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = None
        super().save(*args, **kwargs)
