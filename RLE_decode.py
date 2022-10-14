inp = input().strip()
output = ''
i = 0
cnt = ''

for char in inp:
    if char in '1234567890':
        cnt += char
    elif char not in '1234567890' and cnt.isdigit():
        output += int(cnt) * char
        i += 1
        cnt = ''
    else:
        output += char
        i += 1

print(output)