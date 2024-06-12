from yargy import or_
from gram_utils import sep_rule

from pipelines import (
    OBJECT_HEADER,
    SUBSTRATE_HEADER,
    DETAIL_HEADER
)
from basic_rules import *


DETAIL = sep_rule(
    DETAIL_HEADER, COLON, TEXT, FEATURE_LIST, GEOMETRY, FEATURE
)

SUBSTRATE = sep_rule(
    SUBSTRATE_HEADER, FEATURE, GEOMETRY, FEATURE
)

OBJECT = sep_rule(
    OBJECT_HEADER, or_(DETAIL, SUBSTRATE)
)