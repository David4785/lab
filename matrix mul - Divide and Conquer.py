def add_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]
    return top_left, top_right, bottom_left, bottom_right


def matrix_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    C11 = add_matrices(matrix_multiply(A11, B11), matrix_multiply(A12, B21))
    C12 = add_matrices(matrix_multiply(A11, B12), matrix_multiply(A12, B22))
    C21 = add_matrices(matrix_multiply(A21, B11), matrix_multiply(A22, B21))
    C22 = add_matrices(matrix_multiply(A21, B12), matrix_multiply(A22, B22))

    C = [C11[i] + C12[i] for i in range(mid)] + [C21[i] + C22[i] for i in range(mid)]

    return C


A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = matrix_multiply(A, B)
for row in result:
    print(row)
