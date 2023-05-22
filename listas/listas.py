# criando lista
notas = [7.9, 9.7, 8.2]

# criando listas
lista = []
lista = list()
lista = [26, 'Rafael', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

print(lista[1])

#slices

lista_nova = [10, 20, 30, 40, 50, 60, 70]

print(lista_nova[0:3])
print(lista_nova[3:6])
print(lista_nova[2:])
print(lista_nova[2:6:2])

# percorrer a lista

for elemento in lista_nova:
    print(elemento)

print('Comprimento da lista: ',len(lista_nova))

for i in range(len(lista_nova)):
    print(lista_nova[i])