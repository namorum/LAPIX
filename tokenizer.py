from yargy.tokenizer import Tokenizer, TokenRule


RULES = [
    TokenRule('RU', r'[а-яё]+'),
    TokenRule('LATIN', r'[a-z]+'),
    TokenRule('DATE', r'\d\d[./]\d\d[./]\d\d\d\d'),
    TokenRule('FLOAT', r'\d+[.,]\d+'),
    TokenRule('INT', r'\d+'),
    TokenRule('HYPHEN', r'[-–—]'),
    TokenRule('COLON', r':'),
    TokenRule('PUNCT', r'[\\/!#$%&()\[\]\*\+,\.;?@^_`{|}~№…"\'«»„“ʼʻ”]'),
    TokenRule('EOL', r'\n\t?'),
    TokenRule('EQ', r'[=<>]'),
    TokenRule('OTHER', r'\S')
]


tokenizer = Tokenizer(RULES)