infinity = float('inf')

d = {
    'start': {'A': 6, 'B': 2, 'fin': infinity},
    'A': {'fin': 1},
    'B': {'A': 3, 'fin': 5},
    'fin': {}
}

costs = {'A': 6,
         'B': 2}

parents = {'A': 'start',
           'B': 'start'}

