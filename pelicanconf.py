#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = ''
SITENAME = 'Catalogue de librairies Python pour l\'analyse de données'
SITESUBTITLE = 'University of Mons'
SITEURL = 'https://ecos-umons.github.io'
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = ('%A %d %B %Y')
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'fr'

PATH = 'content'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Override
DEFAULT_CATEGORY = 'misc'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 40  # Set to None to use full content when "Summary" is not specified
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_MENU = False
BOOTSTRAP_FLUID = True #for full width
ARTICLE_ORDER_BY = 'filename'
TEMPLATE_PAGES = {'all.html': 'all.html'}


ARTICLE_PATHS = ['markdowns', 'reread']
STATIC_PATHS = ['static', 'res', 'templates']  # Relative to /content/

THEME = 'themes'  # You should provide static/css/theme.min.js

PLUGIN_PATHS = ['plugins']

JINJA_ENVIRONMENT = { "extensions" : [ "jinja2.ext.i18n"] }
PLUGINS = [ "i18n_subsites" ]
