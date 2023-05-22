# criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Rafael', 'idade': '34', 'altura': '1.72'}

print(dicionario)
print(dicionario['idade'])

# adicionando elementos em um dicionário

dicionario['programador'] = True ## adiciona

print(dicionario) 

dicionario['altura'] = 1.71 ## sobrescreve se já existe

print(dicionario)

# iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# testando se já existe uma chave

print('peso' in dicionario)
print('altura' in dicionario)