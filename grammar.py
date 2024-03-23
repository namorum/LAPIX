from yargy.tokenizer import TokenRule, Tokenizer
from funcs import get_docx_text, regex_between
from yargy import rule

section_headers = [
    'Условия окружающей среды при выполнении технологической операции',
    'Техническое задание на выполнение технологической операции',
    'Оборудование для выполнения технологической операции',
    'Материал для выполнения технологической операции',
    'Ключевые параметры выполнения ТО (процесса)',
    'Характеристики подложки или детали, на которую наносят материал',
    'Рабочая газовая среда',
    'Результат выполнения технологической операции'
]

SECTIONS_EXTRACTION_RULES = [
    TokenRule('Название и общие сведения ТО', regex_between('Протокол технологической операции', 'Условия окружающей среды при выполнении технологической операции'))
]


def tokenize(path):
    text = get_docx_text(path)

    prev_header = ''
    for header in section_headers:
        if header not in text:
            continue
        if prev_header == '':
            prev_header = header
            continue
        SECTIONS_EXTRACTION_RULES.append(
            TokenRule(prev_header, regex_between(prev_header, header))
        )
        prev_header = header
    SECTIONS_EXTRACTION_RULES.append(
        TokenRule(prev_header, regex_between(prev_header, '$'))
    )

    section_tokenizer = Tokenizer(SECTIONS_EXTRACTION_RULES)
    return [SECTIONS_EXTRACTION_RULES, list(section_tokenizer(text))]

    #return(SECTIONS_EXTRACTION_RULES)