# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

try:
    from django.conf.urls import url, patterns
except:
    from django.conf.urls import *

from .views import textareas_js, spell_check, flatpages_link_list, compressor, filebrowser, preview
urlpatterns = [
    url(r'^js/textareas/(?P<name>.+)/$', textareas_js, name='textareas_js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', textareas_js, name='textareas_js'),
    url(r'^spellchecker/$', spell_check, name='spell_check'),
    url(r'^flatpages_link_list/$', flatpages_link_list, name='flatpages_link_list'),
    url(r'^compressor/$', compressor, name='compressor'),
    url(r'^filebrowser/$', filebrowser, name='filebrowser'),
    url(r'^preview/(?P<name>.+)/$', preview, name='preview'),
]
