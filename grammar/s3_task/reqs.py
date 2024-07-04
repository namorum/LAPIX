from yargy import rule
from gram_utils import recursive_interpreted_rule, sep_rule

from pipelines import (
    REQS_HEADER,
    DEFECTS_HEADER,
    MICROSTRUCTURE_HEADER
)
from basic_rules import *

from facts import NonTerm


MICROSTRUCTURE = sep_rule(
    MICROSTRUCTURE_HEADER.interpretation(NonTerm.name), 
    TEXT.interpretation(NonTerm.successors)
).interpretation(NonTerm)

# Требуется, чтобы у дефекта была произвольная вложенность характеристик.
# Здесь это НЕ реализовано.
DEFECT = rule(
    NAME.interpretation(NonTerm.name), 
    HYPHEN, 
    VALUE.interpretation(NonTerm.successors).repeatable(), 
    UNIT.optional().interpretation(NonTerm.successors).repeatable(), EOL, 
    FEATURE_LIST
).interpretation(NonTerm)

DEFECT_LIST = recursive_interpreted_rule(
    DEFECT, NonTerm.successors, EOL, 10
)

DEFECTS = sep_rule(
    DEFECTS_HEADER.interpretation(NonTerm.name), 
    DEFECT_LIST
).interpretation(NonTerm)

REQS = sep_rule(
    REQS_HEADER.interpretation(NonTerm.name), 
    DEFECTS.interpretation(NonTerm.successors).repeatable(), 
    GEOMETRY.interpretation(NonTerm.successors).repeatable(), 
    ELEMENTS.interpretation(NonTerm.successors).repeatable(), 
    MICROSTRUCTURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)