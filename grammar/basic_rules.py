from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from yargy import Parser
import regex as re
from utils import get_docx_text, regex_between, list_to_eq_seq
from gram_utils import sep_rule

from pipelines import (
    NAME, UNIT, ELEMENTS_HEADER, GEOMETRY_HEADER, GRANULOMETRY_HEADER
)
from facts import Node
from gram_utils import recursive_interpreted_rule


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
    and_(type_('INT'), gte(1), lte(31)), 
    in_('/.'), 
    and_(type_('INT'), gte(1), lte(12)), 
    in_('/.'), 
    and_(type_('INT'), gte(1900), lte(3000))
).interpretation(Node.name).interpretation(Node)

NUMBER = or_(
    INT, FLOAT
)

VALUE = or_(
    NUMBER.interpretation(Node.name), 
    NOT_FILLED.interpretation(Node.name)
).interpretation(Node)

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

TEXT_ELEMENT = or_(
    WORD, NUMBER, PUNCT, COLON, HYPHEN
)

TEXT = forward()
TEXT.define(
    or_(
        rule(
            TEXT_ELEMENT, 
            TEXT
        ),
        TEXT_ELEMENT
    )
)

FEATURE = or_(
    rule(
        NAME.interpretation(Node.name), 
        PUNCT, 
        WORDS.interpretation(Node.name).interpretation(Node).interpretation(Node.successors).repeatable()
    ),
    rule(
        NAME.interpretation(Node.name), 
        PUNCT, 
        DATE.interpretation(Node.successors).repeatable()
    ),
    rule(
        NAME.interpretation(Node.name),
        PUNCT.optional(),
        EOL,
        WORDS.interpretation(Node.name).interpretation(Node).interpretation(Node.successors).repeatable()
    ),
    rule(
        NAME.interpretation(Node.name),
        PUNCT,
        DATE.interpretation(Node.successors).repeatable(),
        HYPHEN,
        DATE.interpretation(Node.successors).repeatable()
    ),
    rule(
        NAME.interpretation(Node.name), 
        PUNCT, 
        UNIT.interpretation(Node.name).interpretation(Node).interpretation(Node.successors).repeatable(), 
        PUNCT, 
        VALUE.interpretation(Node.successors).repeatable() 
    ),
    rule(
        WORDS.interpretation(Node.name), 
        PUNCT, 
        VALUE.interpretation(Node.successors).repeatable(), 
        WORD.interpretation(Node.name).interpretation(Node).interpretation(Node.successors).repeatable()
    )
).interpretation(Node)


FEATURE_LIST = recursive_interpreted_rule(
    FEATURE, Node.successors, sep=EOL
)

TEXT_FEATURE = or_(
    rule(
        NAME, COLON, EOL, TEXT
    ),
    rule(
        NAME, COLON, TEXT
    )
)

ELEMENTS = sep_rule(
    ELEMENTS_HEADER, FEATURE_LIST
)

GEOMETRY = sep_rule(
    GEOMETRY_HEADER, FEATURE_LIST
)

GRANULOMETRY_FEATURE = rule(
    eq_("диаметр"), eq_("от"), VALUE, eq_("до"), VALUE, UNIT, HYPHEN, 
    VALUE, UNIT
)

GRANULOMETRY_FEATURE_LIST = recursive_interpreted_rule(
    GRANULOMETRY_FEATURE, None, EOL, 10
)

GRANULOMETRY = sep_rule(
    GRANULOMETRY_HEADER, GRANULOMETRY_FEATURE_LIST
)