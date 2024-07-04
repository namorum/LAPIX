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

from facts import NonTerm


GAS_INFO = rule(
    NUMBER.interpretation(NonTerm.name), 
    PUNCT, EOL, FEATURE_LIST
).interpretation(NonTerm)

GAS_INFO_LIST = recursive_interpreted_rule(
    GAS_INFO, NonTerm.successors, EOL, 5
)

SHIELD_GAS_MIX = sep_rule(
    SHIELD_GAS_MIX_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST, GAS_INFO_LIST
).interpretation(NonTerm)

SINGLE_SHIELD_GAS = sep_rule(
    SINGLE_SHIELD_GAS_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)

SHIELD_GAS = or_(
    SINGLE_SHIELD_GAS, 
    SHIELD_GAS_MIX
)

TRANSPORT_GAS = sep_rule(
    TRANSPORT_GAS_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)

COMPRESSION_GAS = sep_rule(
    COMPRESSION_GAS_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)

GAS_FEED = sep_rule(
    GAS_FEED_HEADER.interpretation(NonTerm.name), 
    SHIELD_GAS.interpretation(NonTerm.successors).repeatable(), 
    TRANSPORT_GAS.interpretation(NonTerm.successors).repeatable(), 
    COMPRESSION_GAS.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)