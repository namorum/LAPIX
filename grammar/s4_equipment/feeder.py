from ..gram_utils import sep_rule
from ..basic_rules import *

from ..pipelines import FEEDER_HEADER

from ..facts import NonTerm


FEEDER = sep_rule(
    FEEDER_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST
).interpretation(NonTerm)