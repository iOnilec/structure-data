# Coleções

# Tuplas
tuple = ('Homo sapiens', 'Canis familiaris', 'Felis catus') # 0, 1, 2

print(tuple)

print(tuple[0])
print(tuple[1])
print(tuple[2])

# Capturar o indice da tupla
print(tuple.index('Felis catus'))

for element in tuple:
    print(element)

# Lista
list_1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
list_2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

# Soma de listas, Juntar duas listas
list_3 =  list_1 + list_2

# Multiplicação de lista, caso precise replicar os dados
list_multi = list_2 * 2

print(list_3)
print(list_multi)
print(list_2[0])
print(list_1[0:3])

# Adicionar item a lista
list_add = list_1.append('Gorila gorila')
print(list_1)

# Remover item na lista
list_del = list_1.remove('Felis catus')
print(list_1)

for i in list_1:
    print(i)