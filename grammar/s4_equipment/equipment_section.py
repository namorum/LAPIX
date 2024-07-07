from ..gram_utils import sep_rule
from ..pipelines import EQUIPMENT_HEADER
from ..basic_rules import FEATURE_LIST, FEATURE
from ..facts import NonTerm

from .feeder import FEEDER

EQUIPMENT_SECTION = sep_rule(
    EQUIPMENT_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST, 
    FEEDER.interpretation(NonTerm.successors)
).interpretation(NonTerm)