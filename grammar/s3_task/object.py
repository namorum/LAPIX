from yargy import or_
from ..gram_utils import sep_rule

from ..pipelines import (
    OBJECT_HEADER,
    SUBSTRATE_HEADER,
    DETAIL_HEADER
)
from ..basic_rules import *

from ..facts import NonTerm


DETAIL = rule(
    DETAIL_HEADER.interpretation(NonTerm.name), 
    COLON, 
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
    EOL, 
    FEATURE.interpretation(NonTerm.successors),
    EOL,
    FEATURE.interpretation(NonTerm.successors),
    EOL,
    GEOMETRY.interpretation(NonTerm.successors),
    EOL, 
    FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)

SUBSTRATE = sep_rule(
    SUBSTRATE_HEADER.interpretation(NonTerm.name), 
    FEATURE.interpretation(NonTerm.successors), 
    GEOMETRY.interpretation(NonTerm.successors), 
    FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)

OBJECT = sep_rule(
    OBJECT_HEADER.interpretation(NonTerm.name), 
    or_(
        DETAIL, 
#        SUBSTRATE
    ).interpretation(NonTerm.successors)
).interpretation(NonTerm)