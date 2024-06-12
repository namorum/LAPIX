from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import sep_rule

from pipelines import COOL_HEADER
from basic_rules import FEATURE_LIST


COOL_SECTION = sep_rule(
    COOL_HEADER, FEATURE_LIST
)