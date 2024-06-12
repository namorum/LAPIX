from yargy import rule
from gram_utils import recursive_interpreted_rule, sep_rule

from pipelines import (
    REQS_HEADER,
    DEFECT_HEADER,
    MICROSTRUCTURE_HEADER
)
from basic_rules import *


MICROSTRUCTURE = sep_rule(
    MICROSTRUCTURE_HEADER, TEXT
)

# Требуется, чтобы у дефекта была произвольная волженность характеристик.
# Здесь это НЕ реализовано.
DEFECT = rule(
    NAME, HYPHEN, VALUE, UNIT.optional(), EOL, 
    FEATURE_LIST
)

DEFECT_LIST = recursive_interpreted_rule(
    DEFECT, None, EOL, 10
)

DEFECTS = sep_rule(
    DEFECT_HEADER, DEFECT_LIST
)

REQS = sep_rule(
    REQS_HEADER, DEFECTS, GEOMETRY, ELEMENTS, MICROSTRUCTURE
)