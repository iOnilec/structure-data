# Coleções 2

# Dicionários
dictionary = {'Aeds aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14} # Nome: Valor
print(dictionary)
print(dictionary['Aeds aegypt'])

# Adicionar elemento ao dicionário
dictionary['Rhodnius montenegrensis'] = 11

# Deletar elemento no dicionário
del(dictionary)['Anopheles darlingi']

# Listar o dicinário em geral
print(dictionary.items())

# Listar chaves do dicionário
print(dictionary.keys())

# Listar valores do dicionário
print(dictionary.values())

dictionary_2 = {'Anopheles gambie': 13, 'Anopheles deaneroum': 14}
print(dictionary_2)

dictionary.update(dictionary_2)

print(dictionary)

for name, value in dictionary.items():
    print(f"Espécie: {name}, número de espécies coletados: {value}")

# Conjuntos
set_1 = ('Proteínas', 'Ácidos nucleicos', 'Carboidrato', 'Lipídeo', 'Proteínas', 'Ácidos nucleicos', 'Carboidrato', 'Lipídeo')

# Não repete objetos dentro do conjunto
print(set(set_1))

set_2 = {1, 2, 3, 4, 5}
set_3 = {3, 4, 5, 6, 7}

# Captura as intercessões nos conjuntos
set_4 = set_2.intersection(set_3)

print(set_4)

# Captura as diferenças nos conjuntos
print(set_3.difference(set_2))
print(set_2.difference(set_3))