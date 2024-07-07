from ..gram_utils import sep_rule
from ..basic_rules import *

from ..pipelines import FEEDER_HEADER

from ..facts import NonTerm


FEEDER = rule(
    FEEDER_HEADER.interpretation(NonTerm.name),
    COLON.optional(),
    EOL, 
    FEATURE_LIST
).interpretation(NonTerm)