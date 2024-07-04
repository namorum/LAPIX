from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import sep_rule

from pipelines import POSITIONING_HEADER
from basic_rules import *


WELD_FOCUS = rule(
    NAME.interpretation(NonTerm.name), 
    COLON, EOL, 
    TEXT.interpretation(NonTerm.successors).interpretation(TermString).interpretation(TermString.value)
).interpretation(NonTerm)

MELT_FOCUS_AXIS = rule(
    NAME.interpretation(NonTerm.name), 
    COLON, EOL, 
    eq_("на"), 
    NUMBER.interpretation(NonTerm.successors).repeatable().interpretation(TermReal).interpretation(TermReal.value), 
    UNIT.interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value), EOL,
    or_(
        eq_("положительное"), eq_("отрицательное")
    ).interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value)
).interpretation(NonTerm)

MELT_FOCUS = or_(
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, EOL, 
        eq_("совмещены").interpretation(NonTerm.successors).interpretation(TermString).interpretation(TermString.value)
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, EOL, 
        eq_("смещены").interpretation(NonTerm.successors).repeatable().interpretation(TermString).interpretation(TermString.value), 
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
    FOCUS_POSITION.interpretation(NonTerm.successors).repeatable(), 
    TEXT_FEATURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)