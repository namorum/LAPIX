from yargy import Parser

from grammar.grammar import DOCUMENT

from tokenizer import tokenizer
from utils import get_docx_text, print_tree


parser = Parser(
    DOCUMENT
)
def parse(file_path='file.docx', rule=DOCUMENT, debug=False):
    parser = Parser(rule)
    input = get_docx_text(file_path)

    if debug:
        print([_.value for _ in tokenizer(input)])
        print('\n\n\n')

        for line in input.splitlines():
            print([_.value for _ in tokenizer(line)])
            #print([_.type for _ in tokenizer(line)])
        print('\n\n\n')

        for match in parser.findall(input):
            print([_.value for _ in match.tokens])
        print('\n\n\n')

        for match in parser.findall(input):
            print_tree(match.fact)
        print('\n\n\n')
    
    return 