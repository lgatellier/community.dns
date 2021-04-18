# -*- coding: utf-8 -*-
#
# Copyright (c) 2017-2021 Felix Fontein
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def format_ttl(ttl):
    sec = ttl % 60
    ttl //= 60
    min = ttl % 60
    ttl //= 60
    h = ttl
    result = []
    if h:
        result.append('{0}h'.format(h))
    if min:
        result.append('{0}m'.format(min))
    if sec:
        result.append('{0}s'.format(sec))
    return ' '.join(result)


class DNSRecord(object):
    def __init__(self):
        self.id = None
        self.type = None
        self.prefix = None
        self.target = None
        self.ttl = 86400  # 24 * 60 * 60
        self.comment = None

    def clone(self):
        result = DNSRecord()
        result.id = self.id
        result.type = self.type
        result.prefix = self.prefix
        result.target = self.target
        result.ttl = self.ttl
        result.comment = self.comment
        return result

    def __str__(self):
        data = []
        if self.id:
            data.append('id: {0}'.format(self.id))
        data.append('type: {0}'.format(self.type))
        if self.prefix:
            data.append('prefix: "{0}"'.format(self.prefix))
        else:
            data.append('prefix: (none)')
        data.append('target: "{0}"'.format(self.target))
        data.append('ttl: {0}'.format(format_ttl(self.ttl)))
        if self.comment is not None:
            data.append('comment: {0}'.format(self.comment))
        return 'DNSRecord(' + ', '.join(data) + ')'

    def __repr__(self):
        return self.__str__()


def format_records_for_output(records, record_name):
    ttls = set([record.ttl for record in records]),
    entry = {
        'record': record_name,
        'type': min([record.type for record in records]) if records else None,
        'ttl': min(*list(ttls)) if records else None,
        'value': [record.target for record in records],
    }
    if len(ttls) > 1:
        entry['ttls'] = ttls
    return entry