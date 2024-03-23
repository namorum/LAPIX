from docx import Document


symbols_to_mirror = ['(', ')']


def get_docx_text(path):
    document = Document(path)
    print(document)
    print()
    paragraphs = []
    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)
    return "\n".join(paragraphs)


# Возвращает регулярку, описывающую текст между строкой x и символом \n.
def regex_before(x):
    for symbol in symbols_to_mirror:
        x = x.replace(symbol, f'\{symbol}')
    return f'(?<={x}\n)(.|\n)*(?=\n)'


# Возвращает регулярку, описывающую текст между строками x1 и x2.
def regex_between(x1, x2, is_strict=False):
    for symbol in symbols_to_mirror:
        x1 = x1.replace(symbol, f'\{symbol}')
        x2 = x2.replace(symbol, f'\{symbol}')
    if is_strict:
        return f'(?<={x1}\n).*?(?={x2})'
    return f'(?<={x1}\n)(.|\n)*(?={x2})'


if __name__ == "__main__":
    print(get_docx_text("file.docx"))