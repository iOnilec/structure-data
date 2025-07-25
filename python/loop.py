# Estrutura de repetição

print(1)
print(2)
print(3)
print(4)
print(5)

# Para o número que esta na faixa de 1 a 6 e depois printa
for number in range(1, 6):
    print(number)

# Para o número que esta na faixa de 5 e 0 ele vai decrementar e depois printa
for number_2 in range(5, 0, -1):
    print(number_2)

# Incrementar
for test in range(2, 7, +1):
    print(test)

# Soma em um loop
sum = 0 # define a var com zero, para armazenar as somas
for number_3 in range(1, 10):
    sum = sum + number_3 # 0 + 1, 1 + 2, 3 + 4...
    print(sum)

numbers = 0 # Inicializo a var como zero
for number_4 in range(0, 101):
    numbers = number_4 # Armazena no loop o intervali de 0 a 101 na váriavel
    print(numbers)

# Percorrer a palavra para achar a letra k
word = 'Goku'
for word_1 in word: # letra na palavra
    if word_1 == 'k': # se for igual 'k'
        print('Achei a letra k') # printa

# Loop em um loop
for i in range(0, 5):
    print(i) # ele printa 0 a 4
    print('----')
    for j in range(0, 3): # loop de 0 a 2
        print(j)
    print()