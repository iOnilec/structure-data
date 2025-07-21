# Manipulação de strings

# string
a = 'oi, mundo!'

print(a)

# Transformar em maiscula
a_upper = a.upper()

print(a_upper)

# Transformar em minuscula
a_lower = a.lower()

print(a_lower)

# Transformar em captalizada
a_capitalize = a.capitalize()

print(a_capitalize)

# Navegação pela string com indices
a_index = a[0:3]

print(a_index)

a_index_last = a[3:]

print(a_index_last)

# Substituição
b = a.replace('mundo!', 'Guto!')

print(b)

print('Meu nome é', b[3:])

# Verificar o tamanho
print(len(b))

# Retirar espaços em brancos de strigs
c = '           Oi '

print(c)

print(c.strip())

# usando outra forma de print com f
n1 = 12452
n2 = 12390

print(f'Dividindo n1 e n2, resultado:', n1 / n2)