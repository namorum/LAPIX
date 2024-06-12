from gram_utils import sep_rule

from pipelines import PREPARE_HEADER
from pre_heat import PRE_HEAT
from basic_rules import *

PREPARE_SECTION = sep_rule(
    PREPARE_HEADER, TEXT_FEATURE, PRE_HEAT 
)
