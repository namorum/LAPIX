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


PARAMS_SECTION = sep_rule(
    PARAMS_HEADER, HEAT, LASER, 
    GAS_FEED, MATERIAL_FEED, 
    POSITIONING, TEXT_FEATURE
)