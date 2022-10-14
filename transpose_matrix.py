"""Need to change transpose func
   to accept non-square matrixes"""


def transpose(bef_matrix):
    """Works only for square matrix"""

    trans_matrix = []
    rows = len(bef_matrix)
    cols = len(bef_matrix[0])

    for row in range(rows):
        trans_matrix.append([0] * cols)

    print(trans_matrix)

    for row in range(rows):
        for col in range(cols):
            trans_matrix[row][col] = bef_matrix[col][row]

    return trans_matrix


def create_matrix(rows: int, cols: int):
    matrix = []
    for row in range(rows):
        matrix.append(input().split())
    return matrix


a, b = map(int, input().split())

t_mtrx = transpose(create_matrix(a, b))

print(t_mtrx)
