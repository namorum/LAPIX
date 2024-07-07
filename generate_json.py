import json
from os.path import join

json_header = {
    "title" : "Архив протоколов технологических операций лазерной обработки (тестовый)",
    "path" : "timerkhanov.ra@students.dvfu.ru / Мой Фонд / Архив протоколов / Архив протоколов технологических операций лазерной обработки$;",
    "json_type" : "universal",
    "ontology" : "vadim@dvo.ru / Мой Фонд / Лазерное аддитивное производство / Онтологии / Онтология архива протоколов технологических операций лазерной обработки$;",
    "name" : "Архив протоколов технологических операций лазерной обработки (тестовый)",
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
                    [
                        {
                            "name" : "Наплавка металлопорошковых материалов на основе олова",
                            "type" : "НЕТЕРМИНАЛ",
                            "successors" :
                            []
                        }
                    ]
                }
            ]
        }
    ]
}


def __tree_to_json(tree):
    output = json_header
    # Если название протокола в нижнем регистре содержит "наплавк", то..., иначе...
    if tree['name'].lower().find("наплавк") > -1:
        output['successors'][0]['name'] = "Наплавка"
    else:
        output['successors'][0]['name'] = "Сварка"
    output['successors'][0]['successors'][0]['successors'][0]['successors'].append(tree)
    output = json.dumps(output, sort_keys=False, indent=4, ensure_ascii=False)
    return output


def generate_json(tree, save_dir):
    if tree is None:
        return None
    json_output = __tree_to_json(tree)
    json_name = f"{tree['name']}.universal.json"
    with open(join(save_dir, json_name), 'w', encoding='utf-8-sig') as file:
        file.write(json_output)
    return json_name
    