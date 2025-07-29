"""
Crie um dicionário para armazenar o nome e a nota de 3 alunos
fazendo a leitura dos valores por meio de uma estrutura de repetição.
Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
"""

students = {
    'Igor Ximenes': 8,
    'Geovanna Demésio': 7.5,
    'Jackson Demésio': 7
}

for student, value in students.items():
    print(f'Aluno: {student} | Média: {value}')

sum = 0
for student, value in students.items():
    sum += value

print(f'A média dos alunos é de: {sum}')