from yargy import rule, or_, and_, not_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from yargy import Parser
import regex as re

from .gram_utils import sep_rule, recursive_interpreted_rule

from .pipelines import (
    NAME, UNIT, ELEMENTS_HEADER, GEOMETRY_HEADER, GRANULOMETRY_HEADER
)
from grammar.facts import NonTerm, TermString, TermReal, TermDate


WORD = rule(
    or_(
        type_('RU'),
        type_('LATIN')
    )
)

COLON = rule(
    type_('COLON')
)

HYPHEN = rule(
    type_('HYPHEN')
)

EQ = rule(
    type_('EQ')
)

PUNCT = rule(
    type_('PUNCT')
)

NOT_FILLED = rule(
    eq_('<'), eq_('не'), eq_('заполнено'), eq_('>')
)

EOL = rule(
    type_('EOL')
)

INT = rule(
    type_('INT')
)

FLOAT = rule(
    type_('FLOAT')
)

DATE = rule(
    type_('DATE')
)

NUMBER = or_(
    FLOAT, INT
)

VALUE = or_(
    NUMBER, NOT_FILLED
)

WORDS = forward()
WORDS.define(
    or_(
        rule(
            WORD, WORDS
        ),
        rule(
            WORD
        ),
        rule(
            NOT_FILLED
        )
    )
)

TEXT = rule(
    not_(type_('EOL')).repeatable()
)

DATE_FEATURE = rule(
    NAME.interpretation(NonTerm.name),
    COLON,
    DATE.interpretation(TermDate.value).interpretation(TermDate).interpretation(NonTerm.successors),
    HYPHEN.optional(),
    DATE.optional().interpretation(TermDate.value).interpretation(TermDate).interpretation(NonTerm.successors)
).interpretation(NonTerm)

FEATURE = or_(
    rule(
        NAME.interpretation(NonTerm.name), 
        PUNCT, 
        UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
        or_(COLON, HYPHEN),
        EQ.optional().interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors),
        rule(
            HYPHEN,
            NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors)
        ).optional(),
        EOL.optional()
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        or_(COLON, HYPHEN), 
        EQ.optional().interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors),
        rule(
            HYPHEN,
            NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors)
        ).optional(),
        UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional()
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional()
    ),
    rule(
        NAME.interpretation(NonTerm.name),
        COLON.optional(),
        EOL,
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional()
    )
).interpretation(NonTerm)

FEATURE_LIST = recursive_interpreted_rule(
    FEATURE, NonTerm.successors, sep=EOL
)

CUSTOM_FEATURE = or_(
    
    rule(
        WORDS.interpretation(NonTerm.name),
        PUNCT, 
        UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors), 
        or_(HYPHEN, COLON, PUNCT), 
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
        EOL.optional()
    ),
    rule(
        WORDS.interpretation(NonTerm.name), 
        or_(PUNCT, COLON, HYPHEN), 
        NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors), 
        WORD.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional()
    ),
    rule(
        WORDS.interpretation(NonTerm.name),
        or_(PUNCT, COLON, HYPHEN),
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
        EOL.optional()
    )
).interpretation(NonTerm)

CUSTOM_FEATURE_LIST = recursive_interpreted_rule(
    CUSTOM_FEATURE, NonTerm.successors, sep=EOL
)

TEXT_FEATURE = or_(
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, EOL, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        COLON, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ),
    rule(
        NAME.interpretation(NonTerm.name), 
        EOL, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    )
).interpretation(NonTerm)

ELEMENTS = sep_rule(
    ELEMENTS_HEADER.interpretation(NonTerm.name), 
    CUSTOM_FEATURE_LIST
).interpretation(NonTerm)

GEOMETRY = sep_rule(
    GEOMETRY_HEADER.interpretation(NonTerm.name),
    FEATURE_LIST
).interpretation(NonTerm)

GRANULOMETRY_FEATURE = rule(
    rule(
        rule(eq_("диаметр")), 
        rule(eq_("от")), 
        NUMBER, 
        rule(eq_("до")), 
        NUMBER, 
        UNIT
    ).interpretation(NonTerm.name), 
    HYPHEN, 
    NUMBER.interpretation(TermReal.value).interpretation(TermReal).interpretation(NonTerm.successors),
    UNIT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
).interpretation(NonTerm)

GRANULOMETRY_FEATURE_LIST = recursive_interpreted_rule(
    GRANULOMETRY_FEATURE, NonTerm.successors, EOL, 10
)

GRANULOMETRY = sep_rule(
    GRANULOMETRY_HEADER.interpretation(NonTerm.name), 
    GRANULOMETRY_FEATURE_LIST
).interpretation(NonTerm)