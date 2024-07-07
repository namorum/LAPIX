from ..gram_utils import sep_rule
from ..basic_rules import *

from ..pipelines import SINGLE_GAS_HEADER

from ..facts import NonTerm


SINGLE_GAS = rule(
    SINGLE_GAS_HEADER.interpretation(NonTerm.name), 
    COLON,
    TEXT.interpretation(TermString.value).interpretation(TermString).interpretation(NonTerm.successors),
    EOL,
    FEATURE_LIST
).interpretation(NonTerm)