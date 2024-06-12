from gram_utils import sep_rule

from pipelines import TASK_HEADER
from object import OBJECT
from material import MATERIAL
from reqs import REQS


TASK_SECTION = sep_rule(
    TASK_HEADER, OBJECT, MATERIAL, REQS
)