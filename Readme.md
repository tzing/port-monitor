# Port monitor

*Port monitor* is a django app provides view and API to check the connection on the specific port of specific server periodically.
It would resolve the monitor target hostname during initialization and test the connection afterward.

![](./screenshot.png)


## Dependency

- django
- dnspython


## Installation

1. Install this app.

    ```bash
    pip install git+https://github.com/tzing/port-monitor.git
    ```

2. Add this app into `INSTALLED_APPS` in `settings.py` of your django project.

    ```py
    INSTALLED_APPS = [
        ...
        'port_monitor.apps.PortMonitorConfig',
    ]
    ```

3. Add path into `urlpatterns` in `urls.py`.

    ```py
    urlpatterns = [
        ...
        path('monitor/', include('port_monitor.urls', namespace='port_monitor')),
    ]
    ```

    Don't forget to import `include`

    ```py
    from django.urls import path, include
    ```

4. Migrate database.

    ```bash
    python manage.py migrate
    ```

5. Optional; [Enable i18n](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/).
(Available language: Traditional Chinese)

6. Done!


## Configuration

**Monitor Target**

Change it in django admin.


**Others**

There is several configs you can change in `settings.py`:

- `DNS_SERVER` (*list* of *str*)

    DNS server to resolve host.
    Default [Cloudflare]'s *1.1.1.1* and *1.0.0.1*.

[Cloudflare]: https://1.1.1.1/

- `DNS_TTL` *(float)*

    Time-to-live value of DNS cache.
    The web page refresh and retry query after this number of seconds.
    Default *3600*.

- `QUERY_INTERVAL` *(float)*

    Seconds between queries. Default *300*.

- `HIGHLIGHT_ROW` *(bool)*

    Highlight entire row of address with the color of current status.
    This feature is useful when one want to view the status from a distance away. Default *False*.

- `JS_TIME_FORMAT` *(str)*

    Time format for showing last/next query time on footer.
    It uses [thdoan/strftime] and please see its [doc] for formatting specifications.
    Default *yyyy/mm/dd(w) HH:MM:SS (GMT+z)* (`%Y/%m/%d(%a) %H:%M:%S (GMT%z)`).

    [thdoan/strftime]: https://github.com/thdoan/strftime/
    [doc]: https://thdoan.github.io/strftime/
