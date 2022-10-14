inp = input().strip()
count = 1

try:
    for i, char in enumerate(inp):
        if char == inp[i + 1]:
            count += 1
        else:
            print(f'{str(count) * (count > 1)}{char}', end='')
            count = 1
except IndexError:
    print(f'{str(count) * (count > 1)}{char}', end='')
