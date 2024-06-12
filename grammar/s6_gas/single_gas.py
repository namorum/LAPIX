from gram_utils import sep_rule
from basic_rules import *

from pipelines import SINGLE_GAS_HEADER


SINGLE_GAS = sep_rule(
    SINGLE_GAS_HEADER, FEATURE_LIST
)