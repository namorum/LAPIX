from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from gram_utils import recursive_interpreted_rule, sep_rule
from basic_rules import *

from pipelines import (
    MATERIAL_FEED_HEADER,
    POWDER_FEED_HEADER,
    POWDER_MIX_FEED_HEADER,
    WIRE_FEED_HEADER
)


MATERIAL_INFO = sep_rule(
    ELEMENTS,
    GRANULOMETRY,
    FEATURE_LIST
)

POWDER_FEED_INFO = sep_rule(
    FEATURE, FEATURE
)

POWDER_FEED = rule(
    POWDER_FEED_HEADER.interpretation(NonTerm.name), 
    COLON, EOL.optional(), 
    TEXT.interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value), 
    EOL,
    MATERIAL_INFO.optional().interpretation(NonTerm.successors).repeatable(), 
    EOL.optional(),
    POWDER_FEED_INFO.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)

ENUM_POWDER = rule(
    NUMBER.interpretation(NonTerm.name), 
    PUNCT, EOL,
    POWDER_FEED.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)

ENUM_POWDER_LIST = recursive_interpreted_rule(
    ENUM_POWDER, NonTerm.successors, EOL, 5
)

POWDER_MIX_FEED = sep_rule(
    POWDER_MIX_FEED_HEADER.interpretation(NonTerm.name), 
    ENUM_POWDER_LIST
).interpretation(NonTerm)

WIRE_FEED_METHOD = or_(
    eq_("центральная").interpretation(TermString).interpretation(TermString.value),
    rule(
        eq_("боковая").interpretation(NonTerm), eq_("под"), eq_("углом"), 
        NUMBER.interpretation(NonTerm.successors).repeatable().interpretation(TermReal).interpretation(TermReal.value), 
        UNIT.interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value)
    )
)

WIRE_FEED_INFO = sep_rule(
    FEATURE.interpretation(NonTerm.successors).repeatable(),
    WIRE_FEED_METHOD.interpretation(NonTerm.successors).repeatable()
)

WIRE_FEED = rule(
    WIRE_FEED_HEADER.interpretation(NonTerm.name), 
    COLON, EOL,
    TEXT.interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value), 
    EOL,
    MATERIAL_INFO.optional().interpretation(NonTerm.successors).repeatable(), EOL.optional(),
    WIRE_FEED_INFO
).interpretation(NonTerm)

MATERIAL_FEED = sep_rule(
    MATERIAL_FEED_HEADER.interpretation(NonTerm.name),
    or_(
        POWDER_FEED,
        POWDER_MIX_FEED,
        WIRE_FEED
    ).interpretation(NonTerm.successors)
).interpretation(NonTerm)