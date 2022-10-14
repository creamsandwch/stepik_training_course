
gen = input()
res = []

for c in gen:
    if res and c == res[-1][0]:
        res[-1][1] += 1
        print(res)
    else:
        res += [[c, 1]]
        print(res)

print(''.join(''.join(str(elem) for elem in sub) for sub in res))
