from yargy import rule, or_, and_, forward
from yargy.tokenizer import TokenRule, Tokenizer
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from yargy import Parser
import regex as re
from funcs import get_docx_text, regex_between, list_to_eq_seq
from pipeline import NAME, UNIT, DOCUMENT_NAME, SECTION_NAME, FEATURE_NAME
from facts import Node


WORD = rule(
    type_('RU')
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


HYPHEN = rule(
    type_('HYPHEN')
)


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

'''
DATES = or_(
    rule(
        DATE.interpretation(DateLeaf.first_date), 
        HYPHEN, 
        DATE.interpretation(DateLeaf.last_date)
    ),
    rule(
        DATE.interpretation(DateLeaf.first_date)
    )
).interpretation(DateLeaf)
'''


FEATURE = forward().interpretation(Node)
FEATURE.define(
    or_(
        rule(
            NAME.interpretation(Node.name), 
            PUNCT, 
            WORDS.interpretation(Node.name).interpretation(Node).interpretation(Node.children).repeatable()
        ),
        rule(
            NAME.interpretation(Node.name), 
            PUNCT, 
            DATE.interpretation(Node.children).repeatable()
        ),
        rule(
            NAME.interpretation(Node.name), 
            PUNCT, 
            DATE.interpretation(Node.children).repeatable(),
            HYPHEN,
            DATE.interpretation(Node.children).repeatable()
        ),
        rule(
            NAME.interpretation(Node.name), 
            PUNCT, 
            UNIT.interpretation(Node.name).interpretation(Node).interpretation(Node.children).repeatable(), 
            PUNCT, 
            VALUE.interpretation(Node.children).repeatable() 
        ),
        rule(
            WORDS.interpretation(Node.name), 
            PUNCT, 
            VALUE.interpretation(Node.children).repeatable(), 
            WORD.interpretation(Node.name).interpretation(Node).interpretation(Node.children).repeatable()
        )
    )
)


SECTION = forward().interpretation(Node)
SECTION.define(
    or_(
        rule(
            FEATURE_NAME.interpretation(Node.name),
            PUNCT,
            WORDS.interpretation(Node.name).interpretation(Node).interpretation(Node.children).repeatable(),
            EOL,
            FEATURE.interpretation(Node.children).repeatable(),
            EOL,
            SECTION
        ),
        rule(
            FEATURE_NAME.interpretation(Node.name),
            EOL,
            FEATURE.interpretation(Node.children).repeatable(),
            EOL,
            SECTION
        ),
        rule(
            FEATURE.interpretation(Node.children).repeatable(),
            EOL,
            SECTION
        ),
        rule(
            FEATURE_NAME.interpretation(Node.name),
            PUNCT,
            WORDS.interpretation(Node.name).interpretation(Node).interpretation(Node.children).repeatable(),
            EOL,
            FEATURE.interpretation(Node.children).repeatable()
        ),
        rule(
            FEATURE_NAME.interpretation(Node.name),
            EOL,
            FEATURE.interpretation(Node.children).repeatable()
        ),
        rule(
            FEATURE.interpretation(Node.children).repeatable()
        )
    )
)


'''
DOCUMENT = forward()
DOCUMENT.define(
    or_(
        rule(
            DOCUMENT_NAME, EOL, WORDS, EOL, SECTION, DOCUMENT
        ),
        rule(
            DOCUMENT_NAME, EOL, SECTION, DOCUMENT
        ),
        rule(
            DOCUMENT_NAME, EOL, SECTION
        )
    )
).named("DOCUMENT")
'''

if __name__ == "__main__":
    parser = Parser(NAME)
