import re
from typing import Any, Generator, Union
from urllib.parse import urlparse, parse_qs

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from config import cookies_file

def is_playlist_url(url) -> bool:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return "list" in query_params

def get_playlist_info(playlist_url: str, cookies: str) -> tuple[str, list]:
    with YoutubeDL({
        'extract_flat': True,
        'cookies': cookies_file(cookies)
    }) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        return playlist_info["title"], playlist_info.get("entries", [])
    
def get_video(video_url: str, cookies: str) -> Union[Any, dict[str, Any], None]:
    with YoutubeDL({
        'cookies': cookies_file(cookies)
    }) as video_ydl:
        return video_ydl.extract_info(video_url, download=False)
   
def extract_timestamps(description: str) -> Generator[Any, Any, None]:
    yield from re.findall(r"(\d{1,2}:\d{2}:\d{2})\s*-\s*(.+)", description)

def time_to_seconds(time_str: str) -> int:
    parts = time_str.split(":")
    seconds = 0
    if len(parts) == 3:
        seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:
        seconds = int(parts[0]) * 60 + int(parts[1])
    return seconds