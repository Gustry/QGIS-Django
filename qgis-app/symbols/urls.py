# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('symbols.views',
        url(r'^$','index'),

        # XML Responses for desktop
        url(r'^tags.xml$','tags'),
        url(r'^tag/(?P<tag>\w+)/$', 'symbols_with_tag'),
        url(r'^authors.xml$', 'authors'),
        url(r'^author/(?P<authid>\d+)/$', 'symbols_by_author'),

        # Form to upload symbols
        url(r'^add/','add_symbol', name='symbol_upload_link'),
        url(r'^up_thanks/', 'upload_thanks')

        )
