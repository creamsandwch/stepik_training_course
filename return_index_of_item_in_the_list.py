lst = input().strip()
lst = lst.split()
number = input()

try:
    for index, value in enumerate(lst):
        break_on_error = lst.index(number)
        if value == number:
            print(f'{index} ', end='')
except ValueError:
    print('None')

