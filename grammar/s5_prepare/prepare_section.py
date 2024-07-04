from gram_utils import sep_rule

from pipelines import PREPARE_HEADER
from pre_heat import PRE_HEAT
from basic_rules import *

from facts import NonTerm


PREPARE_SECTION = sep_rule(
    PREPARE_HEADER.interpretation(NonTerm.name), 
    TEXT_FEATURE.interpretation(NonTerm.successors).repeatable(), 
    PRE_HEAT.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)
