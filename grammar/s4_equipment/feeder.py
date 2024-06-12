from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte

from gram_utils import sep_rule
from basic_rules import *

from pipelines import FEEDER_HEADER


FEEDER = sep_rule(
    FEEDER_HEADER, FEATURE_LIST
)