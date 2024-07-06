from ..gram_utils import sep_rule
from ..basic_rules import *

from ..pipelines import SINGLE_GAS_HEADER

from ..facts import NonTerm


SINGLE_GAS = sep_rule(
    SINGLE_GAS_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)