# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Felix Fontein
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment

    # NOTE: This document fragment needs to be augmented by ZONE_ID_TYPE in a provider document fragment.
    #       The ZONE_ID_TYPE fragment will provide `choices` for the options.type entry.
    DOCUMENTATION = r'''
options:
    what:
        description:
          - Describes whether to fetch a single record and type combination, all types for a
            record, or all records. By default, a single record and type combination is fetched.
          - Note that the return value structure depends on this option.
        choices: ['single_record', 'all_types_for_record', 'all_records']
        default: single_record
        type: str
    zone_name:
        description:
          - The DNS zone to modify.
          - Exactly one of I(zone) and I(zone_id) must be specified.
        type: str
        aliases:
          - zone
    zone_id:
        description:
          - The ID of the DNS zone to modify.
          - Exactly one of I(zone_name) and I(zone_id) must be specified.
    record:
        description:
          - The full DNS record to retrieve.
          - If I(what) is C(single_record) or C(all_types_for_record), exactly one of I(record) and I(prefix) is required.
        type: str
    prefix:
        description:
          - The prefix of the DNS record.
          - This is the part of I(record) before I(zone_name). For example, if the record to be modified is C(www.example.com)
            for the zone C(example.com), the prefix is C(www). If the record in this example would be C(example.com), the
            prefix would be C('') (empty string).
          - If I(what) is C(single_record) or C(all_types_for_record), exactly one of I(record) and I(prefix) is required.
        type: str
    type:
        description:
          - The type of DNS record to retrieve.
          - Required if I(what) is C(single_record).
        type: str

notes:
    - "Supports C(check_mode)."
'''
