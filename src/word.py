
from docx import Document as doc
from docx.shared import Pt
from docx.styles.style import ParagraphStyle
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

def add_hyperlink(paragraph: Paragraph, text: str, url: str, set_bold: bool=False) -> None:
    '''Создаёт гиперссылку.'''
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    
    if set_bold:
        bold = OxmlElement("w:b")
        r_pr.append(bold)
    new_run.append(r_pr)
    text_element = OxmlElement("w:t")
    text_element.text = text
    new_run.append(text_element)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)