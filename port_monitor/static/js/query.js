'use strict';

(function ($) {

    // short cut for
    function log(format, params) {
        var message = format;
        if (typeof message !== 'string') {
            console.log(message);
            return;
        } else if (typeof params !== 'undefined') {
            if (typeof params === 'string') {
                params = [params];
            }
            message = interpolate(format, params);
        }
        var current_time = strftime("%H:%M:%S", new Date())
        console.log(interpolate('[%s] %s', [current_time, message]));
    }

    // resolve DNS, append the IPs on to its card
    $.fn.resolveDNS = function (options) {
        // input check
        if (this.length !== 1 || !this.hasClass('target-card')) {
            log('Error: not only on card given.')
            return;
        }

        // extend options
        options = $.extend({
            defer: $.Deferred()
        }, options);

        // clear existing content
        this.removeClass('text-white bg-danger bg-dark');
        this.find('.card-body').show();
        this.find('.list-group-item').remove();

        var card = this;
        var list_group = this.find('.list-group');

        // if the host is a IP, no extra query is required
        var hostname = this.data('hostname');
        if (hostname.match(/\d+\.\d+\.\d+\.\d+/)) {
            register_address(list_group, hostname);
            this.find('.card-body').hide();
            this.find('.list-group').show();
            options.defer.resolve();
            return;
        }

        // query
        log("resolving %s", hostname);
        $.get(g_port_monitor.ajax.dns_resolve, { host: hostname })
            .done(function (data) {
                $.each(data.address, function (i, addr) {
                    register_address(list_group, addr);
                });
                card.find('.card-body').hide();
                card.find('.list-group').show();
                options.defer.resolve();
            })
            .fail(function (resp) {
                if (resp.status === 0) {
                    card.addClass('text-white bg-dark')
                        .find('.card-body')
                        .text(gettext('Query server is offline'));
                } else {
                    card.addClass('text-white bg-danger')
                        .find('.card-body')
                        .text(interpolate(
                            gettext('Failed to be resolved: %s'),
                            [resp.responseJSON.reason]
                        ));
                    log('Failed to resolve %s', hostname);
                    log(resp.responseJSON);
                }
                options.defer.resolve();
            });
    }

    // assisting func for resolve DNS: add address to card
    function register_address(group, address) {
        var badge = $('<span></span>')
            .addClass('status');

        var message = $('<small></small>')
            .addClass('message');

        var item = $('<li></li>')
            .addClass('address')
            .append(badge)
            .append(address)
            .append(message)
            .data('address', address)
            .setStatus({
                class: 'warning',
                label: gettext('Unknown')
            });

        group.append(item);
    }

    // check connection
    $.fn.checkConnection = function (options) {
        // input check
        if (this.length !== 1 || !this.hasClass('address')) {
            log('Error: not only on card given.')
            return;
        }

        // extend options
        options = $.extend({
            defer: $.Deferred()
        }, options);

        // initialize state
        this.setStatus({
            class: 'warning',
            label: gettext('Checking')
        });

        // query info
        var address = this.data('address');
        var port = this.parents('.card').data('port');
        log("checking %s:%s", [address, port]);

        // query
        var row = this;
        $.get(g_port_monitor.ajax.check_connection, { host: address, port: port })
            .done(function (data) {
                row.setStatus({
                    class: 'success',
                    label: gettext('Up')
                });
                options.defer.resolve();
            })
            .fail(function (resp) {
                if (resp.status === 0) {
                    // query server is off
                    row.setStatus({
                        class: 'dark',
                        label: gettext('Query server is offline')
                    });
                } else {
                    // target server is off
                    row.setStatus({
                        class: 'danger',
                        label: gettext('Down')
                    });
                    row.children('small')
                        .text(resp.responseJSON.reason);
                    log('Failed to query %s', address);
                    log(resp);
                }
                options.defer.resolve();
            });
    };

    // highlight address row
    $.fn.setStatus = function (options) {
        // input check
        if (!this.hasClass('address')) {
            return;
        }

        // default options
        var settings = $.extend({
            class: 'dark',
            label: 'Unspecific',
            message: ''
        }, options);

        // list item
        this.removeClass()
            .addClass('list-group-item address');

        if (g_port_monitor.format.highlight_row) {
            this.addClass('list-group-item-' + settings.class);
        }

        // badge
        this.children('span.status')
            .removeClass()
            .addClass('status badge')
            .addClass('badge-' + settings.class)
            .text(settings.label);

        // append message
        this.children('small.message')
            .text(settings.message);

        return this;
    };

}(jQuery));
