import datetime

from docx import Document as doc
from docx.shared import Pt
from docx.styles.style import ParagraphStyle

from config import output_file
from console_args import ArgsHandler
from word import add_hyperlink
from yt import get_playlist_info, extract_timestamps, time_to_seconds
from log import logger

if __name__ == "__main__":
    logger.info("https://github.com/Sn3ppi/yt-video-parser")
    t1 = datetime.datetime.now()
    args_handler = ArgsHandler()

    info = get_playlist_info(
        args_handler.get_url(), 
        args_handler.get_cookies()
    )
    filename = args_handler.get_name()
    if filename is None:
        filename = info['title']
    d = doc()
    heading = d.add_heading("", level=1)
    add_hyperlink(heading, filename, args_handler.get_url())
    style = d.styles["Normal"]
    if isinstance(style, ParagraphStyle):
        font = style.font
        font.name = "Times New Roman"
        font.size = Pt(11)
        for index, video in enumerate(info['entries'], start=1):
            if isinstance(video, dict):
                title = video['title']
                logger.info(f"{index}. {title}")
                url = video['webpage_url']
                description = video.get('description', '')
                paragraph = d.add_heading(f"{index}. ", level=2)
                add_hyperlink(paragraph, title, url)
                for time, desc in extract_timestamps(description):
                    seconds = time_to_seconds(time)
                    time_url = f"{url}&t={seconds}s"
                    paragraph = d.add_paragraph("")
                    add_hyperlink(paragraph, time, time_url, True)
                    paragraph.add_run(f" - {desc}")
    out = output_file(filename)
    d.save(out)
    t2 = datetime.datetime.now()
    logger.info(f"Документ успешно сохранен: {out}")
    logger.info(f"Затраченное время: {t2-t1}")
    
