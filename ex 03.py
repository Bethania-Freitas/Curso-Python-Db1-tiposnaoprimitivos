#Digite um programa que retonro o maior e o menor item da lista

lista = []
contador = 0

x = int(input("Digite os numeros para colocar na lista:  "))

while contador < x:
    numero = int(input("Digite num número: "))
    lista.append(numero)
    contador += 1

lista.sort()

print(f"O menor valor da lista foi {lista[0]} e o maior valor foi {lista[-1]}")
