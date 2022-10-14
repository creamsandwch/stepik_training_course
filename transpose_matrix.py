
def create_matrix(rows: int):
    """Creates a matrix off of input of rows
       with numbers with a space as a separator"""
    matrix = []
    for row in range(rows):
        matrix.append(input().split())
    return matrix


def create_zero_matrix(rows, cols):
    """
    Returns matrix rows x cols of zeroes
    :param rows: rows of matrix to be created
    :param cols: cols of matrix to be created
    :return: matrix in a form of lists of list
    """
    matrix = []
    for row in range(rows):
        matrix.append([0 for x in range(cols)])
    return matrix


def transpose(bef_matrix):
    """

    :param bef_matrix: matrix in a form of list of lists
    :return: transposed matrix
    """
    rows = len(bef_matrix)
    cols = len(bef_matrix[0])
    trans_matrix = create_zero_matrix(cols, rows)

    for row in range(rows):
        for col in range(cols):
            trans_matrix[col][row] = bef_matrix[row][col]
    return trans_matrix


def print_matrix(matrix):
    rows = len(matrix)
    for row in range(rows):
        print(*matrix[row])


if __name__ == '__main__':
    a, b = map(int, input().split())
    t_mtrx = transpose(create_matrix(a))
    print_matrix(t_mtrx)
