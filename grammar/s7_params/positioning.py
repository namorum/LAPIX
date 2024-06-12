from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import sep_rule

from pipelines import POSITIONING_HEADER
from basic_rules import *


WELD_FOCUS = rule(
    NAME, COLON, EOL, TEXT
)

MELT_FOCUS_AXIS = rule(
    NAME, COLON, EOL, 
    eq_("на"), NUMBER, UNIT, EOL,
    or_(
        eq_("положительное"), eq_("отрицательное")
    )
)

MELT_FOCUS = or_(
    rule(
        NAME, COLON, EOL, eq_("совмещены")
    ),
    rule(
        NAME, COLON, EOL, eq_("совмещены"), EOL,
        MELT_FOCUS_AXIS.optional(), EOL.optional(), MELT_FOCUS_AXIS.optional()
    )
)

FOCUS_POSITION = or_(
    WELD_FOCUS, MELT_FOCUS
)

POSITIONING = sep_rule(
    POSITIONING_HEADER, FEATURE_LIST, FOCUS_POSITION, TEXT_FEATURE
)