"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
"""

def time_and_speed():
    '''
    Função para ler os valores (não recebe parâmetro e retorna os dois valores)
    '''
    time = float(input("Digite o tempo gasto na viagem: "))
    speed = float(input("Digite a velocidade média: "))

    return time, speed

def calc_distance(time, speed):
    '''
    Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
    '''

    return time * speed

def calc_gasoline(distance):
    '''
    Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
    '''
    return distance / 12

def prints(time, speed, distance, used_gasoline):
    '''
    Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
    '''

    print("\n--- RESULTADO DA VIAGEM ---")
    print(f"Velocidade média: {speed:.2f} km/h")
    print(f"Tempo gasto: {time:.2f} horas")
    print(f"Distância percorrida: {distance:.2f} km")
    print(f"Litros de combustível usados: {used_gasoline:.2f} L")

time, speed = time_and_speed()
distance = calc_distance(time, speed)
used_gasoline = calc_gasoline(distance)

prints(time, speed, distance, used_gasoline)