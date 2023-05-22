
# função inicial

def saudacao():
    print('Seja Bem-vindo(a)')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao()

# função com parâmetros

def saudacao_nova(nome: str, curso: str):
    print(f'Seja Bem-vindo(a), {nome}')
    print(f'Olá {nome}, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao_nova('Rafael', 'Python')

# função com parâmetros default

def saudacao_nova(nome: str, curso: str):
    print(f'Seja Bem-vindo(a), {nome}')
    print(f'Olá {nome}, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao_nova('Rafael', 'Python')

# função com retorno

def soma(n1, n2):
    return n1 + n2

resultado = soma(5, 7)

print('O resultado da soma é:', resultado)

def calculadora(n1, n2, operacao: str='+'):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2

resultado = calculadora(10, 20)

print(resultado)