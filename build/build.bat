@echo off
chcp 65001

cd ..
mkdir AppBuild
cd AppBuild
    "C:\Program Files\7-Zip\7z.exe" x "..\packages\ffmpeg-7.1-full_build.7z"
    move ffmpeg-7.1-full_build ffmpeg
    python -m venv pkgs
    call pkgs\Scripts\activate
        pip install -r "..\requirements.txt"
    call pkgs\Scripts\deactivate
    pyinstaller -F --name "YTPlaylistParser" --paths="pkgs/Lib/Site-packages;." --add-data "ffmpeg;ffmpeg" "..\src\main.py"
cd ..
pause