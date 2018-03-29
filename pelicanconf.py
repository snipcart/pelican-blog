#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import listdir
from os.path import isfile, join
import yaml, json, sys

AUTHOR = "Snipcart's geek"
SITENAME = 'A Pelican Blog'
SITEURL = ''
PLUGINS = ['tipue_search.tipue_search'] 
PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Staticman Comments
commentsPath = "./content/comments"

def ymlToJson(file):
    with open(commentsPath + "/" + file) as stream:
        return yaml.load(stream)

commentsYML = [f for f in listdir(commentsPath) if isfile(join(commentsPath, f))]
COMMENTS = list(map(ymlToJson, commentsYML))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
