# Operador condicional

# Se 5 for maior que 3 ele printa!
if 5 > 3:
    print('5 é maior que 3')

# Se 5 for menor que 3 ele printa, caso contrário ele printa outra resposta
if 5 < 3:
    print('5 não é maior que 3')
else:
    print('5 é maior que 3')

# Se 5 for diferente de 3 ele printa, caso contrário ele printa outra coisa
if 5 != 3:
    print('5 é diferente de 3')
else:
    print('5 não é diferente de 3')


n = 11
if n == 9:
    print('N é igual a 9.')
else:
    if n == 10:
        print('N é igual a 10')
    else:
        print('N não é igual a 10 nem 9')

n2 = 4
n3 = 3

# Se uma das condições forem verdadeiras!
if n2 % 2 == 0 or n3 == 4:
    print('O número é par')
else:
    print('O número é impar')

# Se as duas forem verdadeiras!
if n2 % 2 == 0 and n3 == 4:
    print('O número é par')
else:
    print('O número é impar')