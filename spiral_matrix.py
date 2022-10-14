import math

num = int(input().strip())


def func(n):

    offset = 0
    matrix = []

    def transpose(bef_matrix):
        trans_matrix = []

        for c in range(n):
            trans_matrix.append([0] * n)

        for row in range(n):
            for col in range(n):
                trans_matrix[row][col] = bef_matrix[col][row]
        return trans_matrix

    def transpose_second(bef_matrix):
        trans_matrix = []

        for c in range(n):
            trans_matrix.append([0] * n)

        for row in range(n):
            for col in range(n):
                trans_matrix[row][col] = bef_matrix[n - 1 - col][n - 1 - row]
        return trans_matrix

    for cnt in range(n):
        matrix.append([0] * n)

    i = 0
    j = 0
    for elem in range(1, n * n + 1):
        print(f'{j}', 'keek')
        if j + offset < n - 1:
            matrix[i][j + offset] = elem
            j += 1
        else:
            if i + offset < n - 1:
                matrix[i + offset][j] = elem
            else:
                matrix = transpose(matrix)
                matrix = transpose_second(matrix)
                offset += 1
                i = 0
                j = 0
                print()

    print()
    for cnt in range(n):
        print(matrix[cnt])


func(num)
