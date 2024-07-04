from yargy.interpretation import fact, attribute


NonTerm = fact(
    'NonTerm',
    [
        'name',
        attribute('type', 'НЕТЕРМИНАЛ'),
        attribute('successors').repeatable()
    ]
)

TermString = fact(
    'TermString',
    [
        'value',
        attribute('type', 'ТЕРМИНАЛ-ЗНАЧЕНИЕ'),
        attribute('valtype', 'STRING')
    ]
)

TermReal = fact(
    'TermVal',
    [
        'value',
        attribute('type', 'ТЕРМИНАЛ-ЗНАЧЕНИЕ'),
        attribute('valtype', 'REAL')
    ]
)

TermDate = fact(
    'TermVal',
    [
        'value',
        attribute('type', 'ТЕРМИНАЛ-ЗНАЧЕНИЕ'),
        attribute('valtype', 'DATE')
    ]
)