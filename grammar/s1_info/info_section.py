from gram_utils import sep_rule

from pipelines import INFO_HEADER
from basic_rules import TEXT, FEATURE_LIST


INFO_SECTION = sep_rule(
    INFO_HEADER, TEXT, FEATURE_LIST
)