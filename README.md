# Youtube playlist parser to Word docx

Usage:
```shell
YTPlaylistParser "https://www.youtube.com/playlist?list=LINK" -c "cookies.json"
```
All parameters:
```shell
YTPlaylistParser -h
```

```cookies.json``` - your Youtube account browser cookies. Should be placed near YTPlaylistParser.exe.

Output docx file contains playlist name, videos names and their timecodes if present. All the headings and timecodes are clickable.
It can be useful for exam preparation with videolectures.

You can put into YTPlaylistParser.exe directory start.bat file:
```shell
@echo off
chcp 65001

YTPlaylistParser "https://www.youtube.com/playlist?list=LINK" -c "cookies.json"
pause
```