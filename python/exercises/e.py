"""
Ler 5 notas e informar a média
"""

sum = 0
for i in range(5):
    note = float(input('Digite uma nota: '))
    sum += note

media = sum / 5
print(media)


