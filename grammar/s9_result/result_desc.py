from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import recursive_interpreted_rule, sep_rule

from pipelines import (
    RESULT_DESC_HEADER,
    RESULT_GEOMETRY_HEADER,
    RESULT_ELEMENTS_HEADER,
    RESULT_MICROSTRUCTURE_HEADER,
    RESULT_DEFECTS_HEADER
)
from basic_rules import *


RESULT_DEFECT_DESC = rule(
    NAME, COLON, FEATURE, EOL, FEATURE_LIST
)

RESULT_DEFECT_EVAL = rule(
    NAME, COLON, TEXT
)

RESULT_DEFECT = sep_rule(
    NAME, RESULT_DEFECT_DESC, RESULT_DEFECT_EVAL
)

RESULT_DEFECT_LIST = recursive_interpreted_rule(
    RESULT_DEFECT, None, EOL, 10
)

RESULT_GEOMETRY = rule(
    RESULT_GEOMETRY_HEADER, EOL, 
    WORDS, EOL.optional(),
    FEATURE.optional()
)

RESULT_ELEMENTS = sep_rule(
    RESULT_ELEMENTS_HEADER,
    TEXT_FEATURE,
    TEXT_FEATURE
)

RESULT_MICROSTRUCTURE = sep_rule(
    RESULT_MICROSTRUCTURE_HEADER,
    TEXT_FEATURE,
    TEXT_FEATURE
)

RESULT_DEFECTS = sep_rule(
    RESULT_DEFECTS_HEADER, or_(RESULT_DEFECT_LIST, TEXT)
)

RESULT_DESC = sep_rule(
    RESULT_DESC_HEADER,
    RESULT_GEOMETRY,
    RESULT_ELEMENTS,
    RESULT_MICROSTRUCTURE,
    RESULT_DEFECTS,
    TEXT_FEATURE,
    TEXT_FEATURE
)