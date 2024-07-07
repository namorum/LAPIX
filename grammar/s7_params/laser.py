from yargy import rule, or_
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import recursive_interpreted_rule, sep_rule
from ..basic_rules import *

from ..pipelines import (
    LASER_HEADER,
    MODE_HEADER,
    TIMED_POWER_HEADER,
    LAYERED_POWER_HEADER
)

from ..facts import NonTerm, TermReal, TermString


CONTINUAL_MODE = rule(
    eq_('непрерывный').interpretation(TermString.value)
).interpretation(TermString)

NON_CONTINUAL_MODE = sep_rule(
    or_(
        eq_("модулированный").interpretation(TermString.value),
        eq_("импульсный").interpretation(TermString.value)
    ).interpretation(TermString).interpretation(NonTerm.successors),
    FEATURE_LIST
).interpretation(NonTerm)

MODE = rule(
    MODE_HEADER.interpretation(NonTerm.name), 
    COLON, EOL.optional(),
    or_(
        CONTINUAL_MODE, 
#        NON_CONTINUAL_MODE
    ).interpretation(NonTerm.successors)
).interpretation(NonTerm)

T_POWER_FEATURE = rule(
    FEATURE, PUNCT, FEATURE
)

T_POWER_FEATURE_LIST = recursive_interpreted_rule(
    T_POWER_FEATURE, NonTerm.successors, EOL, 10
)

L_POWER_FEATURE = rule(
    rule(
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
        UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ).interpretation(NonTerm.successors).interpretation(NonTerm), 
    rule(
        rule(eq_("для"), or_(eq_("слоев"), eq_("слоёв"))), 
        COLON, eq_("с"), NUMBER, eq_("по"), NUMBER
    ).interpretation(NonTerm.name)
).interpretation(NonTerm)

L_POWER_FEATURE_LIST = recursive_interpreted_rule(
    L_POWER_FEATURE, NonTerm.successors, EOL, 10
)

TL_POWER_FEATURE =  sep_rule(
    T_POWER_FEATURE_LIST, 
    L_POWER_FEATURE_LIST
).interpretation(NonTerm)

TL_POWER_FEATURE_LIST = recursive_interpreted_rule(
    L_POWER_FEATURE, NonTerm.successors, EOL, 10
)

CONSTANT_POWER = rule(
    FEATURE
)

TIMED_POWER = rule(
    TIMED_POWER_HEADER.interpretation(NonTerm.name), 
    COLON.optional(), EOL, 
    T_POWER_FEATURE_LIST
).interpretation(NonTerm)

LAYERED_POWER = rule(
    LAYERED_POWER_HEADER.interpretation(NonTerm.name), 
    COLON.optional(), EOL, 
    L_POWER_FEATURE_LIST
).interpretation(NonTerm)

TIMED_LAYERED_POWER = rule(
    TIMED_POWER_HEADER.interpretation(NonTerm.name), 
    COLON.optional(), EOL, 
    TL_POWER_FEATURE_LIST
).interpretation(NonTerm)

POWER = or_(
    CONSTANT_POWER, 
#    TIMED_POWER, 
#    LAYERED_POWER, 
#    TIMED_LAYERED_POWER
)

LASER = sep_rule(
    LASER_HEADER.interpretation(NonTerm.name), 
    MODE.interpretation(NonTerm.successors), 
    POWER.interpretation(NonTerm.successors), 
    FEATURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)