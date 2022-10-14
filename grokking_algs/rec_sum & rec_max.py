def array_sum(array):
    summary = 0
    if array == []:
        return summary
    else:
        summary += array.pop(0)
    return summary + array_sum(array)


lst = [1, 2]

def array_max(array):
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], array_max(array[1:]))


print(array_max(lst))
