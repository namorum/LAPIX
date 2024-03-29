from docx import Document


symbols_to_mirror = ['(', ')', '/']


def get_docx_text(path):
    document = Document(path)
    print(document)
    print()
    paragraphs = []
    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)
    return "\n".join(paragraphs)


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


if __name__ == "__main__":
    pass