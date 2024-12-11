A = [[1, 2, 3],
     [0, 1, 2],
     [3, 0, 1],]

B = [[1, 2, 3],
     [0, 1, 2],
     [3, 0, 1],]

An = []

n = len(A)
An = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            An[i][j] += A[i][k] * B[k][j]

print (An)