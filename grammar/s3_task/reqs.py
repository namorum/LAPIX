from yargy import rule
from ..gram_utils import recursive_interpreted_rule, sep_rule

from ..pipelines import (
    REQS_HEADER,
    DEFECTS_HEADER,
    MICROSTRUCTURE_HEADER,
    OTHER_FEATURES_HEADER
)
from ..basic_rules import *

from ..facts import NonTerm


OTHER_FEATURES = sep_rule(
    OTHER_FEATURES_HEADER.interpretation(NonTerm.name),
    CUSTOM_FEATURE.repeatable().interpretation(NonTerm.successors)
).interpretation(NonTerm)

MICROSTRUCTURE = sep_rule(
    MICROSTRUCTURE_HEADER.interpretation(NonTerm.name), 
    TEXT.repeatable().interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
).interpretation(NonTerm)

# Требуется, чтобы у дефекта была произвольная вложенность характеристик.
# Здесь это НЕ реализовано.
DEFECT = or_(
    rule(
        WORDS.interpretation(NonTerm.name), 
        HYPHEN, 
        WORDS.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional(), 
        FEATURE_LIST.optional()
    ),
    rule(
        WORDS.interpretation(NonTerm.name), 
        HYPHEN, 
        VALUE.interpretation(NonTerm.successors), 
        UNIT.optional().interpretation(NonTerm.successors), 
        EOL.optional(), 
        FEATURE_LIST.optional()
    )
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
    DEFECTS.optional().interpretation(NonTerm.successors), 
    GEOMETRY.optional().interpretation(NonTerm.successors), 
    ELEMENTS.optional().interpretation(NonTerm.successors), 
    MICROSTRUCTURE.optional().interpretation(NonTerm.successors),
#    OTHER_FEATURES.optional().interpretation(NonTerm.successors)
).interpretation(NonTerm)