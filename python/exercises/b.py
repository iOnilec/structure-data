"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
"""

time_spent = float(input('Digite o tempo gasto na viagem: '))

average_speed = float(input('Digite a velocidade média na viagem: '))

distance = time_spent * average_speed

used_liters = distance / 12

print(f'Tempo gasto na viagem é de', time_spent)
print(f'Velocidade média foi de', average_speed)
print(f'A distância percorrida é de', distance, 'Km')
print(f'A quantidade de combustível usado é de', round(used_liters, 2), 'L')