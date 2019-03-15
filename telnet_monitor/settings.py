from django.conf import settings

TIMEOUT = getattr(settings, 'TIMEOUT', 30)
"""Time out setting to each query.
"""

DNS_SERVER = getattr(settings, 'DNS_TTL', [
    '1.1.1.1',
    '1.0.0.1',
])
"""DNS server address.
"""

DNS_TTL = getattr(settings, 'DNS_TTL', 3600)
"""Time to live value of DNS cache.
"""

QUERY_INTERVAL = getattr(settings, 'QUERY_INTERVAL', 300)
"""Fire a query every N seconds.
"""
