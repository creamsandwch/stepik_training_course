def modify_list(l):
    out = []
    for num in l:
        if num % 2 == 0:
            out.append(num // 2)
    global lst
    lst = out


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
