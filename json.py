import json

json_header = {
    "title" : "Архив протоколов технологических операций лазерной обработки",
    "path" : "timerkhanov.ra@students.dvfu.ru / Мой Фонд / Архив протоколов / Архив протоколов технологических операций лазерной обработки$;",
    "json_type" : "universal",
    "ontology" : "vadim@dvo.ru / Мой Фонд / Лазерное аддитивное производство / Онтологии / Онтология архивапротоколов технологических операций лазерной обработки$;",
    "name" : "Архив протоколов технологических операций лазерной обработки",
    "type" : "КОРЕНЬ",
    "successors" : 
    [
        {
            "name" : "",
            "type" : "НЕТЕРМИНАЛ",
            "successors" :
            [
                {
                    "name" : "Технологическая операция",
                    "type" : "НЕТЕРМИНАЛ",
                    "successors" : []
                }
            ]
        }
    ]
}

def __prepare_output(tree, output):
    output.type = tree.type
    if tree.type == 'НЕТЕРМИНАЛ':
        output.name = tree.name
        output.successors = []
        for successor in tree.successors:
            output.successors.append({})
            __prepare_output(successor, output.successors[-1])
    else:
        output.value = tree.value
        output.valtype = tree.valtype


def __tree_to_json(tree, debug=False):
    if not debug:
        output = json_header
        protocol_name = str(tree.successors[0].name) 
        if protocol_name.find("Наплавк") > -1:
            output.successors[0].name = "Наплавка"
        else:
            output.successors[0].name = "Сварка"
    else:
        output = {}
    __prepare_output(tree, output)

    output = json.dumps(output, sort_keys=True, indent=4)
    if debug:
        print(output)

    return output


def generate_json(tree):
    with open('example.json') as file:
        file.write(__tree_to_json(tree))