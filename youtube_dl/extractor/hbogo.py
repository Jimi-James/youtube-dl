# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class HBOGOIE(InfoExtractor):
    _VALID_URL = r'https?://(?:play\.)?hbogo\.com/(?P<type>(episode|season|extra))/urn:hbo:(?P=type):(?P<id>[a-zA-Z0-9]+)'
    _TESTS = [
        {
            'url': 'http://play.hbogo.com/extra/urn:hbo:extra:GV3QgNQ8DXFvCwgEAAAAa',
            'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
            'info_dict': {
                'id': 'GVtcUtwHMXoiyw9oIAAAG',
                'ext': 'mp4',
                'title': 'Trending Clip: John Oliver on Independence Day',
                'thumbnail': 're:^https?://.*\.jpg$',
                # TODO more properties, either as:
                # * A value
                # * MD5 checksum; start the string with md5:
                # * A regular expression; start the string with re:
                # * Any Python type (for example int or float)
            }
        }
        {
            'url': 'http://play.hbogo.com/episode/urn:hbo:episode:GVtcUtwHMXoiyw9oIAAAG',
            'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
            'info_dict': {
                'id': 'GVtcUtwHMXoiyw9oIAAAG',
                'ext': 'mp4',
                'title': 'Ep 1   The Red Woman',
                'thumbnail': 're:^https?://.*\.jpg$',
                # TODO more properties, either as:
                # * A value
                # * MD5 checksum; start the string with md5:
                # * A regular expression; start the string with re:
                # * Any Python type (for example int or float)
            }
        }
        {
            # Playlist (season) test--very very unfinished (more so than the other 2)
            'url': 'http://play.hbogo.com/season/urn:hbo:season:GVtcUtwKx_pfCwuUIAAAG',
            'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
            'info_dict': {
                'id': 'GVtcUtwKx_pfCwuUIAAAG',
                'ext': 'mp4',
                'title': 'Game of Thrones',
                'thumbnail': 're:^https?://.*\.jpg$',
                # TODO more properties, either as:
                # * A value
                # * MD5 checksum; start the string with md5:
                # * A regular expression; start the string with re:
                # * Any Python type (for example int or float)
            }
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<span style="font-family: Gotham_6r[^"]*"[^>]*>\s*(.+?)\s*</span>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }

