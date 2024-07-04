from gram_utils import sep_rule

from pipelines import EQUIPMENT_HEADER
from basic_rules import FEATURE_LIST
from feeder import FEEDER

from facts import NonTerm


EQUIPMENT_SECTION = sep_rule(
    EQUIPMENT_HEADER.interpretation(NonTerm.name), 
    FEATURE_LIST, 
    FEEDER.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)