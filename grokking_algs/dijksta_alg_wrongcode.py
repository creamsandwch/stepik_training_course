infinity = float('inf')

d = {
    'start': {'A': 6, 'B': 2, 'fin': infinity},
    'A': {'fin': 1},
    'B': {'A': 3, 'fin': 5}
}
parents = {'A': 'start',
           'B': 'start'}


def dijkstra(graph, start_elem, last_elem):
    processed = []
    output = []

    def renew_weights(element, way=0):
        lower = graph[start_elem][last_elem]

        print(set(processed), set(graph.keys()))

        if set(processed) == set(graph.keys()):
            return way
        else:
            processed.append(element)
            for key, value in d[element].items():
                if lower >= value:
                    lower = value
                    next_elem = key
                    processed.append(element)
                    graph[element][next_elem] = value
            way += lower
            print(f'elem = {element} next_elem = {next_elem} lowest = {lower} graph = {graph} way = {way}')
            return way + renew_weights(next_elem)

    return renew_weights(start_elem)


print(dijkstra(d, 'start', 'fin'))
print(dijkstra(d, 'start', 'fin'))
