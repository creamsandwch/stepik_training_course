def binary_search_rec(lst, item, first, last):
    mid = (first + last) // 2

    if lst[mid] < item:
        return binary_search_rec(lst, item, mid + 1, last)
    elif lst[mid] > item:
        return binary_search_rec(lst, item, first, mid - 1)
    else:
        return mid


kek = [c for c in range(1, 13, 2)]
print(kek)

print(binary_search_rec(kek, 11, 0, len(kek)))

