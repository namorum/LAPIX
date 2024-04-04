from yargy.tokenizer import Tokenizer, TokenRule


RULES = [
    TokenRule('RU', r'[а-яё]+'),
    TokenRule('LATIN', r'[a-z]+'),
    TokenRule('INT', r'-?\d+'),
    TokenRule('FLOAT' r'-?\d+[.,]\d+'),
    TokenRule('HYPHEN', r'[-–—]'),
    TokenRule('PUNCT', r'[\\/!#$%&()\[\]\*\+,\.:;<=>?@^_`{|}~№…"\'«»„“ʼʻ”]'),
    TokenRule('EOL', r'\n\t?'),
    TokenRule('OTHER', r'\S'),
]


tokenizer = Tokenizer(RULES)