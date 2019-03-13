import telnetlib
import socket

from django.conf import settings
from django.http import JsonResponse
from dns.resolver import Resolver, NoAnswer


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
    except NoAnswer:
        return JsonResponse({
            'status': 'fail',
            'hostname': hostname,
            'reason': 'no answer',
        }, status=404) # yapf: disable

    return JsonResponse({
        'status': 'success',
        'hostname': hostname,
        'address': [record.address for record in records],
    })


def telnet(request):
    """Connect to server using telnet.
    """
    if 'host' not in request.GET:
        return JsonResponse({
            'status': 'fail',
            'reason': 'hostname not provided',
        }, status=400) # yapf: disable

    hostname = request.GET['host']
    port = request.GET.get('port', 23)
    if isinstance(port, str):
        port = int(port)

    timeout = request.GET.get('timeout', 10)
    if isinstance(timeout, str):
        timeout = int(timeout)

    # query
    try:
        with telnetlib.Telnet(hostname, port, timeout=timeout) as tn:
            ...
    except socket.timeout:
        return JsonResponse({
            'status': 'fail',
            'hostname': hostname,
            'port': port,
            'reason': 'time out',
        }, status=408) # yapf: disable
    except ConnectionRefusedError:
        return JsonResponse({
            'status': 'fail',
            'hostname': hostname,
            'port': port,
            'reason': 'connection refused',
        }, status=403) # yapf: disable

    return JsonResponse({
        'status': 'success',
        'hostname': hostname,
        'port': port,
        'result': 'alive',
    })
