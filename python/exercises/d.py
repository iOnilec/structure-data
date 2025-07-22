"""
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
"""

m1 = float(input('Digite a primeiro nota do aluno: '))
m2 = float(input('Digite a segunda nota do aluno: '))
m3 = float(input('Digite a terceira nota do aluno: '))

average = (m1 + m2 + m3) / 3

print(average)

if average >= 0.0 and average <= 4.0:
    print('REPROVADO!')
elif average >= 4.1 and average <= 6.0:
    print('EXAME!')
    exam = float(input('Digite a nota do exame: '))
    if exam >= 6.0:
        print('APROVADO!')
    else:
        print('REPROVADO!')
elif average > 6.0:
    print('APROVADO!')