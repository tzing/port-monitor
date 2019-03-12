from django.shortcuts import render

from . import models


def monitor(request):
    setting = None
    if models.Setting.objects.exists():
        setting = models.Setting.objects.get()
    else:
        setting = models.Setting()

    return render(request, 'page/monitor.html', {
        'targets': models.MonitorTarget.objects.all(),
        'setting': setting,
    })
