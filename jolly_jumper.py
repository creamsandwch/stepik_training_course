lst = list(map(int, input().split()))

diff = list(range(1, len(lst)))
print(diff)
i = 0

for i in range(len(lst) - 1):
    if abs(lst[i] - lst[i + 1]) in diff:
        diff.pop(diff.index(abs(lst[i] - lst[i + 1])))
    i += 1

print(diff)

if not diff:
    print('Jolly')
else:
    print('Not Jolly')
