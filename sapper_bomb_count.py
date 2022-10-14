nm = input()
n = int(nm.split()[0])
m = int(nm.split()[1])
matrix = []

for i in range(n):
    matrix += [list(input())]

out_matrix = []

for i in range(n + 2):
    out_matrix.append([0] * (m + 2))


for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            for a in range(-1, 2):
                for b in range(-1, 2):
                    out_matrix[i+1+a][j+1+b] += 1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            out_matrix[i+1][j+1] = '*'

for i in range(1, n+1):
    for j in range(1, m+1):
        print(out_matrix[i][j], end='')
    print()


