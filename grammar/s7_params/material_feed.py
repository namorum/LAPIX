from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from gram_utils import recursive_interpreted_rule, sep_rule
from basic_rules import *

from pipelines import MATERIAL_FEED_HEADER


MATERIAL_INFO = rule(
    NAME, HYPHEN, ELEMENTS, EOL,
    NAME, COLON, EOL,
    GRANULOMETRY, EOL,
    FEATURE_LIST
)

POWDER_FEED_INFO = sep_rule(
    FEATURE, FEATURE
)

POWDER_FEED = rule(
    POWDER_FEED_HEADER, COLON, EOL.optional(), 
    NAME, EOL,
    MATERIAL_INFO.optional(), EOL.optional(),
    POWDER_FEED_INFO
)

ENUM_POWDER = rule(
    NUMBER, PUNCT, EOL,
    POWDER_FEED_HEADER, COLON, TEXT, EOL,
    POWDER_FEED_INFO
)

ENUM_POWDER_LIST = recursive_interpreted_rule(
    ENUM_POWDER, None, EOL, 5
)

POWDER_MIX_FEED = sep_rule(
    POWDER_MIX_FEED_HEADER, ENUM_POWDER_LIST
)

WIRE_FEED_METHOD = or_(
    eq_("центральная"),
    rule(
        eq_("боковая"), eq_("под"), eq_("углом"), NUMBER, UNIT
    )
)

WIRE_FEED_INFO = sep_rule(
    FEATURE, WIRE_FEED_METHOD
)

WIRE_FEED = rule(
    WIRE_FEED_HEADER, COLON, EOL,
    NAME, EOL,
    MATERIAL_INFO.optional(), EOL.optional(),
    WIRE_FEED_INFO
)

MATERIAL_FEED = sep_rule(
    MATERIAL_FEED_HEADER,
    or_(
        POWDER_FEED,
        POWDER_MIX_FEED,
        WIRE_FEED
    )
)