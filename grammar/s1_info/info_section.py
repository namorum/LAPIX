from yargy import rule
from yargy.predicates import eq as eq_
from ..gram_utils import sep_rule

from ..pipelines import INFO_HEADER, NAME
from ..basic_rules import TEXT, FEATURE_LIST, EOL, FEATURE, DATE_FEATURE, COLON

from ..facts import NonTerm, TermString


INFO_SECTION = sep_rule(
    INFO_HEADER, 
    TEXT.interpretation(NonTerm.name), 
    rule(
        NAME, 
        COLON, 
        TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors)
    ),
    DATE_FEATURE.interpretation(NonTerm.successors),
    FEATURE.interpretation(NonTerm.successors),
    FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)