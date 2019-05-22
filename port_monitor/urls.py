from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'port_monitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('port_monitor.apiurls', namespace='api')),
    path('jsi18n/',
         JavaScriptCatalog.as_view(packages=['port_monitor']),
         name='javascript-catalog'),
]
