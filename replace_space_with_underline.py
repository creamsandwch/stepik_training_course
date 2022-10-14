import re


def my_solution():
    lst = input().strip().split()
    for word in lst:
        if lst.index(word) < (len(lst) - 1):
            print(f'{word}_', end='')
        else:
            print(word)


def solution_with_regex(inp):
    inp = inp.strip()
    print(re.sub(r'\s+', '_', inp))


solution_with_regex(input())
