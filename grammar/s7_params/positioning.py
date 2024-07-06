from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import sep_rule
from ..pipelines import POSITIONING_HEADER
from ..basic_rules import *


WELD_FOCUS = rule(
    NAME.interpretation(NonTerm.name), 
    COLON, EOL, 
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
).interpretation(NonTerm)

MELT_FOCUS_AXIS = rule(
    NAME.interpretation(NonTerm.name), 
    COLON, EOL, 
    eq_("на"), 
    NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
    UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), EOL,
    or_(
        eq_("положительное"), eq_("отрицательное")
    ).interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
).interpretation(NonTerm)

MELT_FOCUS = or_(
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, EOL, 
        eq_("совмещены").interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, EOL, 
        eq_("смещены").interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
        EOL,
        MELT_FOCUS_AXIS.optional(), EOL.optional(), MELT_FOCUS_AXIS.optional()
    )
).interpretation(NonTerm)

FOCUS_POSITION = or_(
    WELD_FOCUS, MELT_FOCUS
)

POSITIONING = sep_rule(
    POSITIONING_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST, 
    FOCUS_POSITION.interpretation(NonTerm.successors), 
    TEXT_FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)