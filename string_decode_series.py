inp = input().strip()
output = ''

for char in inp:
    index = inp.find(r'\d+[a-zA-Z]')
    output += f'{int(inp[index]) * inp[index+1]}'
    inp = inp[index+2:]

print(output)
