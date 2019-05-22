import socket
import contextlib

from django.http import JsonResponse
from django.shortcuts import render
from dns.resolver import Resolver, NoAnswer, NXDOMAIN
from dns.exception import Timeout

from . import const
from . import models
from . import settings


def index(request):
    context = {
        'targets': models.MonitorTarget.objects.order_by('-order'),
    }

    conf_for_template = [
        'query_interval',
        'timeout',
        'dns_ttl',
        'highlight_row',
        'js_time_format',
        'timeout',
        'dns_server',
    ]

    for conf in conf_for_template:
        context[conf] = getattr(settings, conf.upper())

    return render(request, 'port_monitor/monitor.html', context)


def resolve(request):
    """Resolve host.
    """
    if 'host' not in request.GET:
        return JsonResponse({
            'status': 'fail',
            'reason': 'hostname not provided',
        }, status=400) # yapf: disable

    hostname = request.GET['host']

    # create resolver
    resolver = Resolver()
    resolver.nameservers = settings.DNS_SERVER

    # query
    try:
        records = list(resolver.query(hostname))
        return JsonResponse({
            'status': 'success',
            'hostname': hostname,
            'address': [record.address for record in records],
        })
    except NoAnswer:
        return JsonResponse(
            {
                'status': 'fail',
                'hostname': hostname,
                'reason': 'no answer',
            },
            status=404)
    except NXDOMAIN:
        return JsonResponse(
            {
                'status': 'fail',
                'hostname': hostname,
                'reason': 'query name not exist',
            },
            status=404)
    except (socket.timeout, Timeout):
        return JsonResponse(
            {
                'status': 'fail',
                'hostname': hostname,
                'reason': 'timeout',
            },
            status=408)


def check_connection(request):
    """Try to build a socket to specific port on specific host.
    """
    if 'host' not in request.GET:
        return JsonResponse({
            'status': 'fail',
            'reason': 'hostname not provided',
        }, status=400) # yapf: disable

    host = request.GET['host']

    port = request.GET.get('port', settings.DEFAULT_PORT)
    if isinstance(port, str):
        port = int(port)

    timeout = request.GET.get('timeout', settings.TIMEOUT)
    if isinstance(timeout, str):
        timeout = int(timeout)

    # query
    with contextlib.closing(socket.socket(socket.AF_INET,
                                          socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        errno = sock.connect_ex((host, port))

    if errno == 0:
        return JsonResponse({
            'status': 'success',
            'hostname': host,
            'port': port,
            'result': 'alive',
        })

    else:
        return JsonResponse(
            {
                'status': 'fail',
                'hostname': host,
                'port': port,
                'reason': const.socket_error_code[errno],
            },
            status=400)
