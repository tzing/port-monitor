'use strict';

(function ($) {

    $.fn.status = function (options) {
        // Default options
        var settings = $.extend({
            class: 'dark',
            label: 'Unspecific',
            message: ''
        }, options);

        // list item
        this.removeClass()
            .addClass('list-group-item')

        if (highlight_row) {
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

// datetime formatting
function ftime(d) {
    return strftime(timeformat, d)
}

// dns resolver
var initialize_events = [];
function dns_resolve(elem) {
    var hostname = elem.data('hostname');
    var defer = $.Deferred();
    initialize_events.push(defer);

    if (hostname.match(/\d+\.\d+\.\d+\.\d+/)) {
        register_address(elem, [hostname], defer);
        return;
    }

    $.get('/api/resolve/', { host: hostname })
        .done(function (data) {
            register_address(elem, data.address, defer)
        })
        .fail(function (resp) {
            elem
                .addClass('text-white bg-danger')
                .find('.card-body')
                .text(gettext('Failed to resolve'));
            console.log('Failed to query ' + hostname);
            console.log(resp.responseJSON);
        });
}

// register resolved addresses to card
function register_address(jElem, addresses, defer) {
    // append result
    var group = jElem.find('.list-group');
    $.each(addresses, function (i, addr) {
        var badge = $('<span></span>')
            .addClass('status');

        var message = $('<small></small>')
            .addClass('message');

        var item = $('<li></li>')
            .addClass('list-group-item')
            .append(badge)
            .append(addr)
            .append(message)
            .data('address', addr)
            .status({
                class: 'warning',
                label: gettext('Unknown')
            });

        group.append(item);
    });

    // finalize
    jElem.find('.card-body').remove();
    jElem.find('.list-group').show();
    jElem.data('resolved', true);
    defer.resolve();
}

// query worker
function query_worker() {
    var next_query_time = new Date();
    setInterval(function () {
        var now = new Date();
        var diff_time = next_query_time.getTime() - now.getTime();
        if (diff_time > 0) {
            var fmts = gettext('%s (%s seconds later)');
            var msg = interpolate(fmts, [ftime(next_query_time), Math.ceil(diff_time / 1000)]);
            $('#next-query').text(msg);

            return;
        }

        // update query time
        next_query_time = new Date(now.getTime() + query_interval * 1000);
        $('#last-query').text(ftime(now));
        $('#next-query').text('--');

        // start query
        $('.list-group-item').each(function (idx, elem) {
            var jElem = $(elem)
                .status({
                    class: 'warning',
                    label: gettext('Checking')
                });

            var address = jElem.data('address');
            var port = jElem.parents('.card').data('port');

            $.get('/api/telnet/', { host: address, port: port, timeout: timeout })
                .done(function (data) {
                    jElem.status({
                        class: 'success',
                        label: gettext('Up')
                    });
                })
                .fail(function (resp) {
                    // log
                    console.log('Failed to query ' + address);
                    console.log(resp);

                    if (resp.status === 0) {
                        // query server is off
                        jElem.status({
                            class: 'dark',
                            label: gettext('Query server is offline')
                        });
                    } else {
                        // target server is off
                        jElem.status({
                            class: 'danger',
                            label: gettext('Down')
                        });
                        jElem.children('small')
                            .text(resp.responseJSON.reason);
                    }
                });;
        });

    }, 1000);
}

// start query
$('.card').each(function (idx, elem) { dns_resolve($(elem)); });

$.when.apply($, initialize_events).done(query_worker);
