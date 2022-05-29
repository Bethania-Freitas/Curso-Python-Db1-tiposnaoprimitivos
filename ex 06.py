#Escreva um programa que ordene em ordem crescente uma lista de  tuplas  informadas, pelo último item da  tupla

lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for c in range (len(lista)):
    menor = c
    for j in range (c+1, len(lista)):
        if lista[menor][1] > lista[j][1]:
            menor = j
    lista[c], lista[menor] = lista[menor], lista[c]

print(lista)