from docx import Document
from yargy import rule 
from yargy.predicates import eq as eq_
from yargy.tokenizer import Tokenizer


symbols_to_mirror = ['(', ')', '/']


def get_docx_text(path):
    document = Document(path)
    paragraphs = []
    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)
    text = "\n".join(paragraphs)
    while(text.find("  ") > -1):
        text = text.replace("  ", " ")
    while(text.find("\t\t") > -1):
        text = text.replace("\t\t", "\t")
    while(text.find("\n\n") > -1):
        text = text.replace("\n\n", "\n")
    return text


# Возвращает регулярку, описывающую текст между строками x1 и x2.
def regex_between(x1, x2, is_strict=False, str_end=""):
    if type(x1) is list:
        x1 = f"{str_end}|".join(x1)
    if type(x2) is list:
        x2 = f"|".join(x2)
    x1 += str_end
    for symbol in symbols_to_mirror:
        x1 = x1.replace(symbol, f'\{symbol}')
        x2 = x2.replace(symbol, f'\{symbol}')
    if is_strict:
        return f'(?<={x1}\n).+?(?={x2})'
    return f'(?<={x1}\n)(.|\n)*(?={x2})'
