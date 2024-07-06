from yargy import rule, or_
from ..gram_utils import recursive_interpreted_rule, sep_rule

from ..pipelines import (
    MATERIAL_HEADER,
    WIRE_HEADER,
    POWDER_HEADER,
    GRANULOMETRY_HEADER
)
from ..basic_rules import *

from ..facts import NonTerm, TermString


MATERIAL_INFO = or_(
    rule(
        NUMBER.optional(), PUNCT.optional(), TEXT.interpretation(NonTerm.name), EOL,
        ELEMENTS.optional().interpretation(NonTerm.successors), 
        EOL.optional(),
        GRANULOMETRY.optional().interpretation(NonTerm.successors), 
        EOL.optional(),
        FEATURE_LIST.interpretation(NonTerm.successors)
    ).interpretation(NonTerm),
    rule(
        NUMBER.optional(), PUNCT.optional(),
        TEXT.interpretation(TermString.value)
    ).interpretation(TermString)
)

MATERIAL_INFO_LIST = recursive_interpreted_rule(
    MATERIAL_INFO, NonTerm.successors, EOL, 5
)

POWDER = sep_rule(
    POWDER_HEADER.interpretation(NonTerm.name), 
    COLON, 
    MATERIAL_INFO_LIST
).interpretation(NonTerm)

WIRE = sep_rule(
    WIRE_HEADER.interpretation(NonTerm.name), 
    COLON, 
    MATERIAL_INFO.interpretation(NonTerm.successors)
).interpretation(NonTerm)

MATERIAL = sep_rule(
    MATERIAL_HEADER.interpretation(NonTerm.name), 
    or_(POWDER, WIRE).interpretation(NonTerm.successors)
).interpretation(NonTerm)
