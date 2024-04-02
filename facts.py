from yargy.interpretation import fact, attribute


Node = fact(
    'Node',
    [attribute('name', None),
     attribute('unit', None),
     attribute('value', None),
     attribute('children', None).repeatable()
    ]
)

Leaf = fact(
    'Leaf', 
    [
        'name', 
        attribute('unit', None), 
        'value'
    ]
)

DateLeaf = fact(
    'DateLeaf',
    [
        'first_date', 
        attribute('last_date', None),
        attribute('children', None)
    ]
)