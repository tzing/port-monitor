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

HIGHLIGHT_ROW = getattr(settings, 'HIGHLIGHT_ROW', False)
"""Highlight entire row of address with the color of current status.
This feature is useful when one want to view the status from a distance away.
"""

JS_TIME_FORMAT = getattr(settings, 'JS_TIME_FORMAT',
                         "%Y/%m/%d(%a) %H:%M:%S (GMT%z)")
"""Time format for the last/next query time on footer.
See https://thdoan.github.io/strftime/ for specifications.
"""
