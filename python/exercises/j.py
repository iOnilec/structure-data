"""
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
C é a temperatura em graus Celsius.

- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão
"""

def celsius_to_fahrenheit_no_param():
    '''
    Conversão de celsius para fahrenheit (Função sem parâmetro)
    '''
    C = float(input("Digite a temperatura em grau celsius: "))

    F = (9 * C + 160) / 5
    print(F)
celsius_to_fahrenheit_no_param()

def celsius_to_fahrenheit_param(c):
    '''
    Conversão de celsius para fahrenheit (Função com parâmtro de graus celsius)
    '''
    return (9 * c + 160) / 5
F = celsius_to_fahrenheit_param(20)
print(F)

def celsius_to_fahrenheit_param_and_print(c):
    '''
    Conversão de celsius para fahrenheit (Função com parâmtro de graus celsius)
    e a impressão do resultado
    '''
    F = (9 * c + 160) / 5
    print(F)
celsius_to_fahrenheit_param_and_print(20)