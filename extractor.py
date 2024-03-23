from yargy import interpretation, parser
from yargy import rule, or_ 
from funcs import get_docx_text, regex_between
from terminals import NAMES, UNITS, SECTION_NAMES, FEATURE_NAMES


NAME = or_(
    
)


def extract(path):
    text = get_docx_text(path)
    