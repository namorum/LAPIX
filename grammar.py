from IPython.display import display
import IPython

IPython.embed()

from yargy import rule, or_, forward
from yargy.tokenizer import TokenRule
from funcs import get_docx_text, regex_between
from terminals import NAMES, UNITS, SECTION_NAMES, FEATURE_NAMES


def list_to_rules(list):
    rules = []
    for el in list:
        rules.append(rule(el))
    return tuple(rules)


VALUE = TokenRule(
    "VALUE",
    f"({regex_between(NAMES, ' *\n| *\t', is_strict=True, str_end=': ')})|({regex_between(UNITS, ' *\n| *\t', is_strict=True, str_end=': ')})"
)

FEATURE_VALUE = TokenRule(
    "FEATURE_VALUE",
    regex_between(FEATURE_NAMES, " *\n| *\t", is_strict=True, str_end=": ")
)


COMMA = rule(
    ","
).named("COMMA")

COLON = rule(
    ": "
).named("COLON")

NEWLINE = or_(
    rule(
        "\n"
    ),
    rule(
        "\t"
    )
).named("NEWLINE")

NAME = or_(
    *list_to_rules(NAMES)
).named("NAME")

UNIT = or_(
    *list_to_rules(UNITS)
).named("UNIT")

SECTION_NAME = or_(
    *list_to_rules(SECTION_NAMES)
).named("SECTION_NAME")

FEATURE_NAME = or_(
    *list_to_rules(FEATURE_NAMES)
).named("FEATURE_NAME")


SUBFEATURE = forward()
SUBFEATURE.define(
    or_(
        rule(
            NAME, COLON, VALUE, NEWLINE
        ),
        rule(
            NAME, COMMA, UNIT, COLON, VALUE, NEWLINE
        )
    )
).named("SUBFEATURE")

FEATURE = forward()
FEATURE.define(
    or_(
        rule(
            SUBFEATURE, FEATURE
        ),
        rule(
            SUBFEATURE
        )
    )
).named("FEATURE")

SECTION = forward()
SECTION.define(
    or_(
        rule(
            FEATURE_NAME, FEATURE_VALUE, FEATURE, SECTION
        ),
        rule(
            FEATURE_NAME, FEATURE_VALUE, FEATURE
        )
    )
).named("SECTION")

DOCUMENT = forward()
DOCUMENT.define(
    or_(
        rule(
            SECTION_NAME, SECTION, DOCUMENT
        ),
        rule(
            SECTION_NAME, SECTION
        )
    )
).named("DOCUMENT")


if __name__ == "__main__":
    display(DOCUMENT.normalized.as_bnf)
    
    