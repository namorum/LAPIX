from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from gram_utils import recursive_interpreted_rule, sep_rule
from basic_rules import *

from pipelines import GAS_MIX_HEADER

from facts import NonTerm


GAS_INFO = rule(
    NUMBER.interpretation(NonTerm.name), PUNCT, EOL, 
    FEATURE_LIST
).interpretation(NonTerm)

GAS_INFO_LIST = recursive_interpreted_rule(
    GAS_INFO, NonTerm.successors, EOL, 5
)

GAS_MIX = sep_rule(
    GAS_MIX_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST, 
    GAS_INFO_LIST
).interpretation(NonTerm)