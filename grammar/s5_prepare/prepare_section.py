from ..gram_utils import sep_rule
from ..pipelines import PREPARE_HEADER
from ..basic_rules import *
from ..facts import NonTerm

from .pre_heat import PRE_HEAT

PREPARE_SECTION = sep_rule(
    PREPARE_HEADER.interpretation(NonTerm.name), 
    TEXT_FEATURE.interpretation(NonTerm.successors), 
    PRE_HEAT.interpretation(NonTerm.successors)
).interpretation(NonTerm)
