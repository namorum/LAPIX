from yargy import Parser
from docx import Document

from tokenizer import tokenizer

from grammar.grammar import *

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


def print_json_tree(tree, indent=0):
    if tree['type'] == 'НЕТЕРМИНАЛ':
        print(f"{'\t'*indent*2}{tree['name']}")
        print(f"{'\t'*indent*2}{tree['type']}", end='\n\n')
        for successor in tree['successors']:
            print_json_tree(successor, indent+1)
    else:
        print(f"{'\t'*indent*2}{tree['value']}")
        print(f"{'\t'*indent*2}{tree['type']}")
        print(f"{'\t'*indent*2}{tree['valtype']}", end='\n\n')


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
    
    tree = parser.find(input).fact

    json_like = {}
    __tree_to_json_like(tree, json_like)
    

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
    print_json_tree(document_tree)
    return document_tree
