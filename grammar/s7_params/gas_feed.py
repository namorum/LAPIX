from yargy import rule, or_
from gram_utils import recursive_interpreted_rule, sep_rule

from pipelines import (
    GAS_FEED_HEADER,
    SINGLE_SHIELD_GAS_HEADER,
    SHIELD_GAS_MIX_HEADER,
    TRANSPORT_GAS_HEADER,
    COMPRESSION_GAS_HEADER
)
from basic_rules import *


GAS_INFO = rule(
    NUMBER, PUNCT, EOL, FEATURE_LIST
)

GAS_INFO_LIST = recursive_interpreted_rule(
    GAS_INFO, None, EOL, 5
)

SHIELD_GAS_MIX = sep_rule(
    SHIELD_GAS_MIX_HEADER, FEATURE_LIST, GAS_INFO_LIST
)

SINGLE_SHIELD_GAS = sep_rule(
    SINGLE_SHIELD_GAS_HEADER, FEATURE_LIST
)

SHIELD_GAS = or_(
    SINGLE_SHIELD_GAS, SHIELD_GAS_MIX
)

TRANSPORT_GAS = sep_rule(
    TRANSPORT_GAS_HEADER, FEATURE_LIST
)

COMPRESSION_GAS = sep_rule(
    COMPRESSION_GAS_HEADER, FEATURE_LIST
)

GAS_FEED = sep_rule(
    GAS_FEED_HEADER, SHIELD_GAS, TRANSPORT_GAS, COMPRESSION_GAS
)