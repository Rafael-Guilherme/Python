# print(int(input('Qual é a sua idade?')))

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


media = float(input('Informe a média do estudadante: '))

if media >= 7:
    print('Você foi aprovada(o)')
elif media >=5:
    print('Recuperação')
else:
    print('Você foi reprovada(o)')


nota_final = 10
presenca = 60

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')