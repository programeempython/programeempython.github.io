# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'http://programeempython.com.br'
TIMEZONE = 'Europe/Copenhagen'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
RSS_FEED_SUMMARY_ONLY = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_TAG = "G-CWQ34LZTCX"

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-5019623326305470',
    'page_level_ads': True,
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}

DISQUS_SITENAME = "programeempython"
WITH_FUTURE_DATES = False
