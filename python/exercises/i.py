"""
Dada a matriz abaixo construa uma estrutura de repetição para percorrer e somar 
todos os elementos da matriz
"""

import numpy as np

matrix = np.array([[3, 4, 1],
                   [3, 1, 5]])

sum = 0
for i in range(matrix.shape[0]):
    print(matrix[i]) # Linha
    for j in range(matrix.shape[1]):
        print(matrix[i][j]) # Item individual
        sum += matrix[i][j]

print(sum)