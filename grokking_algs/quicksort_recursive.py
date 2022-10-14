def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [c for c in array[1:] if c < pivot]
        greater = [c for c in array[1:] if c >= pivot]
        print(f'less={less} greater={greater} pivot={pivot}')
        return quicksort(less) + [pivot] + quicksort(greater)


kek = [1, 10, 512, 4, -2, 0, 10]

print(quicksort(kek))
print(f'sorted={sorted(kek)}')