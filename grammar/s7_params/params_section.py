from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import sep_rule

from pipelines import PARAMS_HEADER
from heat import HEAT
from laser import LASER
from gas_feed import GAS_FEED
from material_feed import MATERIAL_FEED
from positioning import POSITIONING
from basic_rules import *

from facts import NonTerm


PARAMS_SECTION = sep_rule(
    PARAMS_HEADER.interpretation(NonTerm.name), 
    HEAT.interpretation(NonTerm.successors).repeatable(), 
    LASER.interpretation(NonTerm.successors).repeatable(), 
    GAS_FEED.interpretation(NonTerm.successors).repeatable(), 
    MATERIAL_FEED.interpretation(NonTerm.successors).repeatable(), 
    POSITIONING.interpretation(NonTerm.successors).repeatable(), 
    TEXT_FEATURE.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)