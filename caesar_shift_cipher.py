shift = int(input())
message = input().strip()
output = ''

shift = shift % 27

for char in message:
    new_index = ' abcdefghijklmnopqrstuvwxyz'.index(char) + shift
    output += ' abcdefghijklmnopqrstuvwxyz'[new_index]

print(f'Result: "{output}"')

