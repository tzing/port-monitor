from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TelnetMonitorConfig(AppConfig):
    name = 'telnet_monitor'
    verbose_name = _('Telnet Monitor')
