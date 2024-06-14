from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from gram_utils import recursive_interpreted_rule, sep_rule
from basic_rules import *

from pipelines import (
    LASER_HEADER,
    MODE_HEADER,
    TIMED_POWER_HEADER,
    LAYERED_POWER_HEADER
)

CONTINUAL_MODE = rule(
    eq_('непрерывный')
)

NON_CONTINUAL_MODE = sep_rule(
    or_(eq_("модулированный"), eq_("импульсный")),
    FEATURE_LIST
)

MODE = sep_rule(
    MODE_HEADER, or_(CONTINUAL_MODE, NON_CONTINUAL_MODE)
)

T_POWER_FEATURE = rule(
    FEATURE, PUNCT, FEATURE
)

T_POWER_FEATURE_LIST = recursive_interpreted_rule(
    T_POWER_FEATURE, None, EOL, 10
)

L_POWER_FEATURE = rule(
    NUMBER, UNIT, eq_("для"), or_(eq_("слоев"), eq_("слоёв")), 
    COLON, eq_("с"), NUMBER, eq_("по"), NUMBER
)

L_POWER_FEATURE_LIST = recursive_interpreted_rule(
    L_POWER_FEATURE, None, EOL, 10
)

TL_POWER_FEATURE =  sep_rule(
    T_POWER_FEATURE_LIST, 
)

TL_POWER_FEATURE_LIST = recursive_interpreted_rule(
    L_POWER_FEATURE, None, EOL, 10
)

CONSTANT_POWER = rule(
    FEATURE
)

TIMED_POWER = rule(
    TIMED_POWER_HEADER, COLON.optional(), EOL, T_POWER_FEATURE_LIST
)

LAYERED_POWER = rule(
    LAYERED_POWER_HEADER, COLON.optional(), EOL, L_POWER_FEATURE_LIST
)

TIMED_LAYERED_POWER = rule(
    TIMED_POWER_HEADER, COLON.optional(), EOL, TL_POWER_FEATURE_LIST
)

POWER = or_(
    CONSTANT_POWER, TIMED_POWER, 
    LAYERED_POWER, TIMED_LAYERED_POWER
)

LASER = sep_rule(
    LASER_HEADER, MODE, POWER, FEATURE_LIST
)