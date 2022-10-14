import collections

inp = input().strip().lower().split()

cnt = collections.Counter(inp)

for key, value in cnt.items():
    print(key, value)
