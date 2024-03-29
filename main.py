from funcs import get_docx_text
from parse import parser


input = get_docx_text('file.docx')
print(input)

output = parser.findall(input)
print(output)


for match in output:
    print([_.value for _ in match.tokens])
