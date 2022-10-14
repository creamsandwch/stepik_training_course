inp = input().split()
a, b = int(inp[0]), int(inp[1])

for elem in range(a, b + 1):
    if elem % 3 == 0 and elem % 5 == 0:
        print('FizzBuzz')
    elif elem % 3 == 0:
        print('Fizz')
    elif elem % 5 == 0:
        print('Buzz')
    else:
        print(elem)