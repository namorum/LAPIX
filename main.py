from utils import get_docx_text, print_tree
from tokenizer import tokenizer
from parse import parse

from grammar.s1_info.info_section import INFO_SECTION
from grammar.s2_condition.condition_section import CONDITION_SECTION
from grammar.s3_task.task_section import TASK_SECTION
from grammar.s4_equipment.equipment_section import EQUIPMENT_SECTION
from grammar.s5_prepare.prepare_section import PREPARE_SECTION
from grammar.s6_gas.gas_section import GAS_SECTION
from grammar.s7_params.params_section import PARAMS_SECTION
from grammar.s8_cool.cool_section import COOL_SECTION
from grammar.s9_result.result_section import RESULT_SECTION

from grammar.basic_rules import FEATURE, TEXT, DATE_FEATURE


#parse("grammar//tests//INFO.docx", INFO_SECTION, True)
#parse("grammar//tests//CONDITION.docx", CONDITION_SECTION, True)
parse("grammar//tests//TASK.docx", TASK_SECTION, True)
#parse("grammar//tests//EQUIPMENT.docx", EQUIPMENT_SECTION, True)
#parse("grammar//tests//PREPARE.docx", PREPARE_SECTION, True)
#parse("grammar//tests//GAS.docx", GAS_SECTION, True)
#parse("grammar//tests//PARAMS.docx", PARAMS_SECTION, True)
#parse("grammar//tests//COOL.docx", COOL_SECTION, True)
#parse("grammar//tests//RESULT.docx", RESULT_SECTION, True)
