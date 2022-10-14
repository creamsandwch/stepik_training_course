from collections import deque

d = {}
d['name1'] = ['n1', 'n2']
d['n1'] = ['name1']
d['n2'] = ['name1', 'n4', 'n5']
d['n4'] = ['n2']
d['n5'] = ['n2', 'mango']
print(d.items())


def wide_search(name, graph):
    step = 0
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(f'{person}, {step}')
        step += 1
        if not person in searched:
            if person == 'mango':
                print(f'result = {person}')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


wide_search('name1', d)
