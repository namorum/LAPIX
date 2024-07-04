from yargy import rule, or_, and_, forward
from yargy.predicates import eq as eq_, type as type_, in_, gte, lte
from gram_utils import sep_rule

from pipelines import RESULT_HEADER
from result_desc import RESULT_DESC
from basic_rules import *

from facts import NonTerm


RESULT_SECTION = sep_rule(
    RESULT_HEADER.interpretation(NonTerm.name), 
    TEXT_FEATURE.interpretation(NonTerm.successors), 
    RESULT_DESC.interpretation(NonTerm.successors)
).interpretation(NonTerm)