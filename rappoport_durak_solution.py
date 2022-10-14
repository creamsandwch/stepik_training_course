(c1, c2), m = input().replace('10', 'T', 2).split(), input()
r1 = (c1[1] == m, '6789TJQKA'.find(c1[0]) * (c1[1] == c2[1]))
r2 = (c2[1] == m, '6789TJQKA'.find(c2[0]) * (c1[1] == c2[1]))
ans = 0 if r1 > r2 else 1 if r1 < r2 else 2
print(['First', 'Second', 'Error'][ans])