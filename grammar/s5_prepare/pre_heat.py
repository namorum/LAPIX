from ..gram_utils import sep_rule
from ..basic_rules import *

from ..pipelines import PRE_HEAT_HEADER

from ..facts import NonTerm


PRE_HEAT = sep_rule(
    PRE_HEAT_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)