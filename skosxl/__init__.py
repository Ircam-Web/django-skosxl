# -*- coding: utf-8 -*-

from __future__ import unicode_literals


VERSION = (0, 3)

def get_version():
    return '%s.%s' % (VERSION[0], VERSION[1])

__version__ = get_version()

default_app_config = 'skosxl.apps.SKOSXLConfig'
