from gram_utils import sep_rule

from pipelines import EQUIPMENT_HEADER
from basic_rules import FEATURE_LIST
from feeder import FEEDER


EQUIPMENT_SECTION = sep_rule(
    EQUIPMENT_HEADER, FEATURE_LIST, FEEDER
)