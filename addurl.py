#!/usr/bin/env python3
#
# ./addurl.py http://aria2:6800/rpc http://video.url
#

import youtube_dl
from xmlrpc import client
import sys

ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    test_url = sys.argv[2]
    info = ydl.extract_info(test_url, download=False)

# Get Title
title = info['title']

if info.get('requested_formats') is not None:
    # we got DASH formats
    video_format, audio_format = info['requested_formats']
    video_url = video_format['url']
    video_ext = video_format['ext']
    audio_url = audio_format['url']
    audio_ext = audio_format['ext']
elif info.get('entries') is not None:
    video_entry = info['entries']
    video_url = video_entry[0]['url']
    video_ext = video_entry[0]['ext']
else:
    video_url = info['url']
    video_ext = info['ext']

s = client.ServerProxy(sys.argv[1])
s.aria2.addUri([video_url], dict(out=title + "." + video_ext))
