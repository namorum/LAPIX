from yargy import rule, or_
from yargy.predicates import type as type_


'''
Генерирует интерпретированную правую часть правил конечной рекурсии следующего вида.
left -> right + sep + left | right
'''
def recursive_interpreted_rule(right, right_interpretation=None, sep=None, max_recursion_depth=10):
    if right_interpretation is not None:
        right = rule(right.interpretation(right_interpretation))
    
    list_of_right_rules = []
    for cur_len in reversed(range(1, max_recursion_depth+1)):
        if sep is None:
            right_rule_args = [right] * cur_len
        else:
            right_rule_args = [right, sep] * (cur_len - 1)
            right_rule_args.append(right)
        list_of_right_rules.append(rule(*right_rule_args))
    
    return or_(*list_of_right_rules)


def sep_rule(*args, sep=rule(type_('EOL')).optional()):
    new_args = []
    for el in args:
        new_args.append(el)
        new_args.append(sep)
    new_args.pop()
    new_args = tuple(new_args)
    return rule(*new_args)