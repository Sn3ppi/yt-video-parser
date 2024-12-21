import os
import sys

from log import logger

OUT_DIR = os.getcwd()
if getattr(sys, 'frozen', False):
    ROOT_DIR = sys._MEIPASS
else:
    ROOT_DIR = OUT_DIR
os.environ["PATH"] += os.pathsep + os.path.abspath(os.path.join(ROOT_DIR, "ffmpeg", "bin"))

def output_file(filename: str) -> str:
    return os.path.join(OUT_DIR, f"{filename}.docx")

def cookies_file(filepath: str) -> str:
    cookies = os.path.join(OUT_DIR, filepath)
    if not os.path.exists(cookies):
        logger.error(f"cookies path {cookies} not found!")
    return os.path.join(OUT_DIR, filepath)
