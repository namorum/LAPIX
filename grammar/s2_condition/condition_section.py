from gram_utils import sep_rule

from pipelines import CONDITION_HEADER
from basic_rules import FEATURE_LIST

from facts import NonTerm


CONDITION_SECTION = sep_rule(
    CONDITION_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)