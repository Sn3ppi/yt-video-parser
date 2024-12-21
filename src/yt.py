import re
from typing import Generator, Any

from yt_dlp import YoutubeDL

from config import cookies_file

def get_playlist_info(playlist_url: str, cookies: str) -> (Any | dict[str, Any] | None):
    '''Возвращает информацию о плейлисте.'''
    with YoutubeDL({
        'extract_flat': False,
        'cookies': cookies_file(cookies),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor'
        }]
    }) as ydl:
        return ydl.extract_info(playlist_url, download=False)
    
def extract_timestamps(description: str) -> Generator[Any, Any, None]:
    '''Извлекает таймкоды.'''
    yield from re.findall(r"(\d{1,2}:\d{2}:\d{2})\s*-\s*(.+)", description)

def time_to_seconds(time_str: str) -> int:
    '''Преобразовывает время формата ЧЧ:ММ:СС в секунды.'''
    parts = time_str.split(":")
    seconds = 0
    if len(parts) == 3:
        seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:
        seconds = int(parts[0]) * 60 + int(parts[1])
    return seconds