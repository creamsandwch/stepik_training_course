import collections

inp = input().strip().split()

cnt = collections.Counter(inp)

for key, value in cnt.items():
    if value > 1:
        print(key, '', end=' ')