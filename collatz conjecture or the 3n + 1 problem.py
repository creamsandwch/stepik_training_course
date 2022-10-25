
def collatz(x: int):
    if x == 1:
        print(x)
    else:
        print(x, '', end='')
        while x != 1:
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1
            print(f'{x:.0f}', '', end='')


collatz(int(input()))