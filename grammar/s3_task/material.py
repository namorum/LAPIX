from yargy import rule, or_
from gram_utils import recursive_interpreted_rule, sep_rule

from pipelines import (
    MATERIAL_HEADER,
    WIRE_HEADER,
    POWDER_HEADER,
    GRANULOMETRY_HEADER
)
from basic_rules import *




MATERIAL_INFO = or_(
    rule(
        NUMBER.optional(), PUNCT.optional(), TEXT, EOL,
        NAME, COLON, EOL,
        ELEMENTS, EOL,
        NAME, COLON, EOL,
        GRANULOMETRY, EOL,
        FEATURE_LIST
    ),
    TEXT
)

MATERIAL_INFO_LIST = recursive_interpreted_rule(
    MATERIAL_INFO, None, EOL, 5
)

POWDER = sep_rule(
    POWDER_HEADER, COLON, MATERIAL_INFO_LIST
)

WIRE = sep_rule(
    WIRE_HEADER, COLON, MATERIAL_INFO
)

MATERIAL = sep_rule(
    MATERIAL_HEADER, or_(POWDER, WIRE)
)
