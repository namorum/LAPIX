from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import recursive_interpreted_rule, sep_rule
from ..basic_rules import *

from ..pipelines import (
    MATERIAL_FEED_HEADER,
    POWDER_FEED_HEADER,
    POWDER_MIX_FEED_HEADER,
    WIRE_FEED_HEADER
)


MATERIAL_INFO = sep_rule(
    ELEMENTS.interpretation(NonTerm.successors),
    GRANULOMETRY.interpretation(NonTerm.successors)
)

POWDER_FEED_INFO = rule(
    FEATURE.interpretation(NonTerm.successors).repeatable()
)

POWDER_FEED = rule(
    POWDER_FEED_HEADER.interpretation(NonTerm.name), 
    COLON, EOL.optional(), 
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
    EOL,
#    MATERIAL_INFO.optional(),      - это место вызывало RecursionError
#    EOL.optional(),                - и это
    POWDER_FEED_INFO
).interpretation(NonTerm)

ENUM_POWDER = rule(
    NUMBER.interpretation(NonTerm.name), 
    PUNCT, EOL,
    POWDER_FEED.interpretation(NonTerm.successors)
).interpretation(NonTerm)

ENUM_POWDER_LIST = recursive_interpreted_rule(
    ENUM_POWDER, NonTerm.successors, EOL, 5
)

POWDER_MIX_FEED = sep_rule(
    POWDER_MIX_FEED_HEADER.interpretation(NonTerm.name), 
    ENUM_POWDER_LIST
).interpretation(NonTerm)

WIRE_FEED_METHOD = or_(
    rule(eq_("центральная")).interpretation(TermString.value).interpretation(TermString),
    rule(
        rule(eq_("боковая")).interpretation(NonTerm.name), eq_("под"), eq_("углом"), 
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
        UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ).interpretation(NonTerm)
)

WIRE_FEED_INFO = sep_rule(
    FEATURE.interpretation(NonTerm.successors),
    WIRE_FEED_METHOD.interpretation(NonTerm.successors)
)

WIRE_FEED = rule(
    WIRE_FEED_HEADER.interpretation(NonTerm.name), 
    COLON, EOL,
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
    EOL,
    MATERIAL_INFO.optional().interpretation(NonTerm.successors), EOL.optional(),
    WIRE_FEED_INFO
).interpretation(NonTerm)

MATERIAL_FEED = sep_rule(
    MATERIAL_FEED_HEADER.interpretation(NonTerm.name),
    or_(
        POWDER_FEED,
#        POWDER_MIX_FEED,
#        WIRE_FEED
    ).interpretation(NonTerm.successors)
).interpretation(NonTerm)