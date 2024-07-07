from yargy import rule, or_, forward
from .basic_rules import EOL
from .gram_utils import recursive_interpreted_rule, sep_rule

from .facts import NonTerm

from .s1_info.info_section import INFO_SECTION
from .s2_condition.condition_section import CONDITION_SECTION
from .s3_task.task_section import TASK_SECTION
from .s4_equipment.equipment_section import EQUIPMENT_SECTION
from .s5_prepare.prepare_section import PREPARE_SECTION
from .s6_gas.gas_section import GAS_SECTION
from .s7_params.params_section import PARAMS_SECTION
from .s8_cool.cool_section import COOL_SECTION
from .s9_result.result_section import RESULT_SECTION


DOCUMENT = sep_rule(
#    INFO_SECTION,
#    CONDITION_SECTION.interpretation(NonTerm.successors),
#    TASK_SECTION.interpretation(NonTerm.successors),
    EQUIPMENT_SECTION.interpretation(NonTerm.successors),
    PREPARE_SECTION.interpretation(NonTerm.successors),
    GAS_SECTION.interpretation(NonTerm.successors),
    PARAMS_SECTION.interpretation(NonTerm.successors),
    COOL_SECTION.interpretation(NonTerm.successors),
    RESULT_SECTION.interpretation(NonTerm.successors)
).interpretation(NonTerm)