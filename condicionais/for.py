
"""for i in range(10):
    print(i)"""

# for i in range(1, 5):
#     print(i)

"""for i in range(0, 10, 2):
    print(i)"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota

print(soma / 3)