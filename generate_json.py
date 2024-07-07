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
                    "name" : "Ремонтное восстановление детали",
                    "type" : "НЕТЕРМИНАЛ",
                    "successors" :
                    []
                }
            ]
        }
    ]
}


def __tree_to_json(tree):
    output = json_header
    # Если название протокола в нижнем регистре содержит "наплавк", то..., иначе...
    if tree['successors'][0]['value'].lower().find("наплавк") > -1:
        output['successors'][0]['name'] = "Наплавка"
    else:
        output['successors'][0]['name'] = "Сварка"
    tree['name'] = 'Наплавка металлопорошковых материалов на основе олова'      # Временная мера, пока не дадут право на добавление новых классов ТО
    output['successors'][0]['successors'][0]['successors'].append(tree)
    output = json.dumps(output, sort_keys=False, indent=4, ensure_ascii=False)

    return output


def generate_json(tree):
    json_output = __tree_to_json(tree)
    with open(f'{tree['successors'][0]['value']}.universal.json', 'w', encoding='utf-8-sig') as file:
        file.write(json_output)