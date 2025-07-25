# Estrutura de repetição 2

number = 1
while number < 6: # Enquanto numero for menor que 6
    print(number) # ele printa
    number += 1 # Incrementa e repete o processo

number_2 = 5
while number_2 > 0:
    print(number_2)
    number_2 -= 1

sum = 0
number_3 = 0
while number_3 < 10:
    sum += number_3 # 0 + 0, 0 + 1, 1 + 2, 3 + 3, 6 + 4...
    number_3 += 1 # incrementa 1
print(sum)

number_4 = -1
while number_4 < 1 or number_4 > 10: # Enquanto número for menor que 1 e maior que 10 ele atribui o input
    number_4 = int(input('Digite um número entre 1 a 10: '))