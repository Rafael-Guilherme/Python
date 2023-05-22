numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

"""if numero_sorteado == numero_escolhido:
    print('você acertou!')
else:
    print('você errou!')"""

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns! Você acertou!')

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1