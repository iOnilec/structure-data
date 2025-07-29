"""
Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
"""

int_nums = [1, 5, 7, 9, 3]

for n in int_nums:
    print(n)

sum = 0
for i in int_nums:
    sum += i

print(sum)

