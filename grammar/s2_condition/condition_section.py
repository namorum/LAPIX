from gram_utils import sep_rule

from pipelines import CONDITION_HEADER
from basic_rules import FEATURE_LIST


CONDITION_SECTION = sep_rule(
    CONDITION_HEADER, FEATURE_LIST
)