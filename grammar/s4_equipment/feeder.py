from gram_utils import sep_rule
from basic_rules import *

from pipelines import FEEDER_HEADER


FEEDER = sep_rule(
    FEEDER_HEADER, FEATURE_LIST
)