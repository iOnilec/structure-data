# Matrizes

import numpy as np

matrix = np.array([[2, 3, 1], 
                   [4, 5, 7], 
                   [6, 8, 0],
                   [12, 45, 22]])

print(matrix)

# Listar número de linhas e elementos
print(matrix.shape)

# Listar os indices na matriz com linha e o item
print(matrix[1][2])

# Percorre todas as linhas e colunas de uma matriz, utilizando shape
for i in range(matrix.shape[0]):
    print(matrix[i])
    for j in range(matrix.shape[1]): # Cada elemento individual
        print(matrix[i][j])
