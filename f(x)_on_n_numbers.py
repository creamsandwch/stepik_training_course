import functools

count = int(input().strip())
d = {}


def f(x):
    return x ** 2


@functools.lru_cache(maxsize=None)
def g(x):
    return f(x)


for i in range(count):
    d[i] = g(int(input().strip()))

for i in range(count):
    print(d[i])
