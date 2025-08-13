# Funções

# Funções em parâmetro e sem retorno
def message():
    print('Oi, Mundo')

message()
message()
message()

# Função com passagem de parâmetro
def message0(text):
    print(text)

message0('Oi, Mundo!')
message0('Meu nome é')
message0('Guto')

def sum(a, b):
    print(a + b)

sum(12, 12)

# Função com passagem de parâmetro e retorno
def sum0(c, d):
    return c + d

r = sum0(34, 34)
print(r)

def calc_gravi_pot_energy(m, h, g = 10):
    '''
    Insira a descrição da função
    '''
    e = g * m * h
    return e
r2 = calc_gravi_pot_energy(30, 12)
print(r2)