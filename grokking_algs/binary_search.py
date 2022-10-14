def binary_search(array, item):
    start = 0
    end = len(array) - 1

    for i in range(len(array) - 1):
        print(array[i], ' ', end='')
    print()
    for i in range(len(array) -1):
        print(i, ' ', end='')
    print('\n')

    while start <= end:
        mid = (start + end) // 2
        print(f'mid={mid} start={start} end={end}')
        guess = array[mid]
        print(f'array[mid]={guess}')

        if guess == item:
            return mid

        if guess < item:
            start = mid + 1
        else:
            end = mid - 1

    return None


print(binary_search([c for c in range(1, 12, 2)], 7))
