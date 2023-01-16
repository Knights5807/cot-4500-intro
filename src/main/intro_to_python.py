import numpy as np

# Generates 2 random matrices of size 3x3
matrix_1 = np.random.randint(0, 10, size=(3, 3))
matrix_2 = np.random.randint(0, 10, size=(3, 3))

# If row num equal col num, set equal to 1, else 0
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            matrix_1[i, j] = 1
        elif i != j:
            matrix_1[i, j] = 0

# If row num equal col num, cell equals matrix_1, else equals matrix_1 + 3
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            matrix_2[i, j] = matrix_1[i, j]
        elif i != j:
            matrix_2[i, j] = matrix_1[i, j] + 3

# Prints each matrix with a space inbetween
print(matrix_1)
print('')
print(matrix_2)
print('')

# Cuts last col off of matrix_2
print(matrix_2[:, 0:2])
