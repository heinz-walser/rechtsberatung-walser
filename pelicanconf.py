#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = { 'sidebar': sidebar }

AUTHOR = u'Heinz Walser'
SITENAME = u'Heinz Walser, pat. Rechtsagent'
SITEURL = u'http://localhost:8000'
RELATIVE_URLS = True
PATH = u'content'
TIMEZONE = u'Europe/Zurich'
DEFAULT_LANG = u'en'
CATEGORYICONS = ''
USE_FOLDER_AS_CATEGORY = True
# nice themes
# - html5-dopetrope
# - twenty-html5up
THEME = "./.themes/Flex"

PLUGIN_PATHS = ["./.plugins"]
#PLUGINS = ['tipue_search']
STATIC_PATHS = ['resources']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
