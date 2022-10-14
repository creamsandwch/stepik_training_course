states_needed = {c for c in 'abcdefgm'}

stations = {
    'col': {'a', 'b', 'c'},
    'mag': {'b', 'e', 'd'},
    'lst': {'e', 'f', 'g'},
    'kek': {'a', 'g'},
    'obz': {'m'}
}

stations_included = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered_on_step = states & states_needed
        if len(covered_on_step) > len(states_covered):
            best_station = station

        states_needed -= covered_on_step
        print(states_needed)
        stations_included.add(best_station)

print(stations_included)