from yargy import or_
from gram_utils import sep_rule

from pipelines import (
    OBJECT_HEADER,
    SUBSTRATE_HEADER,
    DETAIL_HEADER
)
from basic_rules import *

from facts import NonTerm


DETAIL = sep_rule(
    DETAIL_HEADER.interpretation(NonTerm.name), 
    COLON, 
    TEXT.interpretation(NonTerm.successors).repeatable(), 
    FEATURE_LIST, 
    GEOMETRY.interpretation(NonTerm.successors).repeatable(), 
    FEATURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)

SUBSTRATE = sep_rule(
    SUBSTRATE_HEADER.interpretation(NonTerm.name), 
    FEATURE.interpretation(NonTerm.successors).repeatable(), 
    GEOMETRY.interpretation(NonTerm.successors).repeatable(), 
    FEATURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)

OBJECT = sep_rule(
    OBJECT_HEADER.interpretation(NonTerm.name), 
    or_(DETAIL, SUBSTRATE).interpretation(NonTerm.successors)
).interpretation(NonTerm)