from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'telnet_monitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('telnet_monitor.apiurls', namespace='api')),
    path(
        'jsi18n/',
        JavaScriptCatalog.as_view(packages=['telnet_monitor']),
        name='javascript-catalog'),
]
