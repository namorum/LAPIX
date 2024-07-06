from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from ..gram_utils import sep_rule
from ..basic_rules import *
from ..facts import NonTerm
from ..pipelines import PARAMS_HEADER

from .heat import HEAT
from .laser import LASER
from .gas_feed import GAS_FEED
from .material_feed import MATERIAL_FEED
from .positioning import POSITIONING



PARAMS_SECTION = sep_rule(
    PARAMS_HEADER.interpretation(NonTerm.name), 
    HEAT.interpretation(NonTerm.successors), 
    LASER.interpretation(NonTerm.successors), 
    GAS_FEED.interpretation(NonTerm.successors), 
    MATERIAL_FEED.interpretation(NonTerm.successors), 
    POSITIONING.interpretation(NonTerm.successors), 
    TEXT_FEATURE.interpretation(NonTerm.successors)
).interpretation(NonTerm)