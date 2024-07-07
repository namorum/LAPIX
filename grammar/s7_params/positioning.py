from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import sep_rule
from ..pipelines import (
    POSITIONING_HEADER, 
    MELT_FOCUS_HEADER,
    WELD_FOCUS_HEADER,
    HORIZONTAL_SHIFT_HEADER,
    MELT_FOCUS_AXIS_HEADER
)
from ..basic_rules import *


HORIZONTAL_SHIFT = rule(
    HORIZONTAL_SHIFT_HEADER.interpretation(NonTerm.name), 
    COLON, EOL, 
    or_(
        rule(
            eq_('отсутствует')
        ).interpretation(TermString.value).interpretation(TermString),
        rule(
            rule(eq_('присутствует')).interpretation(NonTerm.name), 
            eq_('('), 
            NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
            UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
            eq_(')')
        ).interpretation(NonTerm)
    ).interpretation(NonTerm.successors)
).interpretation(NonTerm)

WELD_FOCUS = rule(
    WELD_FOCUS_HEADER.interpretation(NonTerm.name), 
    COLON, EOL, 
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
).interpretation(NonTerm)

MELT_FOCUS_AXIS = rule(
    MELT_FOCUS_AXIS_HEADER.interpretation(NonTerm.name), 
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
        MELT_FOCUS_HEADER.interpretation(NonTerm.name), 
        COLON, EOL, 
        eq_("совмещены").interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ),
    rule(
        MELT_FOCUS_HEADER.interpretation(NonTerm.name), 
        COLON, EOL, 
        rule(
            eq_("смещены").interpretation(NonTerm.name), 
            EOL,
            MELT_FOCUS_AXIS.optional().interpretation(NonTerm.successors), 
            EOL.optional(), 
            MELT_FOCUS_AXIS.optional().interpretation(NonTerm.successors)
        ).interpretation(NonTerm).interpretation(NonTerm.successors)
    )
).interpretation(NonTerm)

FOCUS_POSITION = or_(
#    WELD_FOCUS, 
    MELT_FOCUS
)

POSITIONING = sep_rule(
    POSITIONING_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST,
    HORIZONTAL_SHIFT.interpretation(NonTerm.successors),
    FEATURE.interpretation(NonTerm.successors),
    FOCUS_POSITION.interpretation(NonTerm.successors)
).interpretation(NonTerm)