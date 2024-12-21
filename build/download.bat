@echo off
chcp 65001

mkdir packages
cd packages
curl -L -O https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-7.1-full_build.7z
cd ..
pause