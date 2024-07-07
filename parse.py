from yargy import Parser
from docx import Document

from tokenizer import tokenizer

from grammar.grammar import DOCUMENT

from grammar.s1_info.info_section import INFO_SECTION
from grammar.s2_condition.condition_section import CONDITION_SECTION
from grammar.s3_task.task_section import TASK_SECTION
from grammar.s4_equipment.equipment_section import EQUIPMENT_SECTION
from grammar.s5_prepare.prepare_section import PREPARE_SECTION
from grammar.s6_gas.gas_section import GAS_SECTION
from grammar.s7_params.params_section import PARAMS_SECTION
from grammar.s8_cool.cool_section import COOL_SECTION
from grammar.s9_result.result_section import RESULT_SECTION


def get_docx_text(path):
    document = Document(path)
    paragraphs = []
    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)
    text = "\n".join(paragraphs)
    while(text.find("  ") > -1):
        text = text.replace("  ", " ")
    while(text.find("\t\t") > -1):
        text = text.replace("\t\t", "\t")
    while(text.find("\n\n") > -1):
        text = text.replace("\n\n", "\n")
    return text


def print_tree(tree, indent=0):
    if tree.type == 'НЕТЕРМИНАЛ':
        print(f'{'\t'*indent*2}{tree.name}')
        print(f'{'\t'*indent*2}{tree.type}', end='\n\n')
        for successor in tree.successors:
            print_tree(successor, indent+1)
    else:
        print(f'{'\t'*indent*2}{tree.value}')
        print(f'{'\t'*indent*2}{tree.type}')
        print(f'{'\t'*indent*2}{tree.valtype}', end='\n\n')


def __tree_to_json_like(tree, json_like):
    if tree.type == 'НЕТЕРМИНАЛ':
        json_like['name'] = tree.name
        json_like['type'] = tree.type
        json_like['successors'] = []
        for successor in tree.successors:
            json_like['successors'].append({})
            __tree_to_json_like(successor, json_like['successors'][-1])
    else:
        if tree.valtype == 'REAL':
            json_like['value'] = float(tree.value)
        elif tree.valtype == 'DATE':
            json_like['value'] = tree.value + '-00:00:00.000'
        else:
            json_like['value'] = tree.value
        json_like['type'] = tree.type
        json_like['valtype'] = tree.valtype


def parse_rule(file_path, rule):
    parser = Parser(rule, tokenizer=tokenizer)
    input = get_docx_text(file_path)
    
    json_like = {}
    __tree_to_json_like(parser.find(input).fact, json_like)
    del parser

    return json_like


def parse_document(file_path):
    document_tree = parse_rule(file_path, INFO_SECTION)
    if document_tree == {}:
        return None
    for rule in [
        CONDITION_SECTION, 
        TASK_SECTION, 
        EQUIPMENT_SECTION, 
        PREPARE_SECTION, 
        GAS_SECTION, 
        PARAMS_SECTION, 
        COOL_SECTION, 
        RESULT_SECTION
        ]:
        document_tree['successors'].append({})
        document_tree['successors'][-1] = parse_rule(file_path, rule)
    return document_tree
