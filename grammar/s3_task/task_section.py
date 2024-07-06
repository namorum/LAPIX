from ..gram_utils import sep_rule
from ..pipelines import TASK_HEADER
from ..facts import NonTerm

from .object import OBJECT
from .material import MATERIAL
from .reqs import REQS

TASK_SECTION = sep_rule(
    TASK_HEADER.interpretation(NonTerm.name), 
    OBJECT.interpretation(NonTerm.successors), 
    MATERIAL.interpretation(NonTerm.successors), 
    REQS.interpretation(NonTerm.successors)
).interpretation(NonTerm)