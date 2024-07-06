from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import recursive_interpreted_rule, sep_rule
from ..pipelines import (
    RESULT_DESC_HEADER,
    RESULT_GEOMETRY_HEADER,
    RESULT_ELEMENTS_HEADER,
    RESULT_MICROSTRUCTURE_HEADER,
    RESULT_DEFECTS_HEADER
)
from ..basic_rules import *
from ..facts import NonTerm, TermString


RESULT_DEFECT_DESC = rule(
    NAME.interpretation(NonTerm.name), 
    COLON,
    FEATURE_LIST
).interpretation(NonTerm)

RESULT_DEFECT_EVAL = rule(
    NAME.interpretation(NonTerm.name), 
    COLON, 
    TEXT.interpretation(NonTerm.successors)
).interpretation(NonTerm)

RESULT_DEFECT = sep_rule(
    NAME.interpretation(NonTerm.name), 
    RESULT_DEFECT_DESC.interpretation(NonTerm.successors), 
    RESULT_DEFECT_EVAL.interpretation(NonTerm.successors)
).interpretation(NonTerm)

RESULT_DEFECT_LIST = recursive_interpreted_rule(
    RESULT_DEFECT, NonTerm.successors, EOL, 10
)

RESULT_GEOMETRY = rule(
    RESULT_GEOMETRY_HEADER.interpretation(NonTerm.name), 
    EOL, 
    WORDS.interpretation(NonTerm.successors), 
    EOL.optional(),
    FEATURE.optional().interpretation(NonTerm.successors)
).interpretation(NonTerm)

RESULT_ELEMENTS = sep_rule(
    RESULT_ELEMENTS_HEADER.interpretation(NonTerm.name),
    TEXT_FEATURE.interpretation(NonTerm.successors),
    TEXT_FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)

RESULT_MICROSTRUCTURE = sep_rule(
    RESULT_MICROSTRUCTURE_HEADER.interpretation(NonTerm.name),
    TEXT_FEATURE.interpretation(NonTerm.successors),
    TEXT_FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)

RESULT_DEFECTS = sep_rule(
    RESULT_DEFECTS_HEADER.interpretation(NonTerm.name), 
    or_(
        RESULT_DEFECT_LIST, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    )
).interpretation(NonTerm)

RESULT_DESC = sep_rule(
    RESULT_DESC_HEADER.interpretation(NonTerm.name),
    RESULT_GEOMETRY.interpretation(NonTerm.successors),
    RESULT_ELEMENTS.interpretation(NonTerm.successors),
    RESULT_MICROSTRUCTURE.interpretation(NonTerm.successors),
    RESULT_DEFECTS.interpretation(NonTerm.successors),
    TEXT_FEATURE.interpretation(NonTerm.successors),
    TEXT_FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)