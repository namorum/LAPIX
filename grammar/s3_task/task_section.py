from gram_utils import sep_rule

from pipelines import TASK_HEADER
from object import OBJECT
from material import MATERIAL
from reqs import REQS

from facts import NonTerm


TASK_SECTION = sep_rule(
    TASK_HEADER.interpretation(NonTerm.name), 
    OBJECT.interpretation(NonTerm.successors).repeatable(), 
    MATERIAL.interpretation(NonTerm.successors).repeatable(), 
    REQS.interpretation(NonTerm.successors).repeatable()
).interpretation(NonTerm)