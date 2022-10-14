def binary_search_recursive(list1, element):
    if len(list1) == 0:
        return False
    else:
        mid = len(list1)//2
        if element == list1[mid]:
            return mid
        else:
            if element > list1[mid]:
                return binary_search_recursive(list1[mid+1:], element)
            else:
                return binary_search_recursive(list1[:mid], element)


kek = [c for c in range(1, 15, 2)]

print(kek)

print(binary_search_recursive(kek, 1))

