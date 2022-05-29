#Escreva um programa que some todos os itens de uma lista.

lista = []
contador = 0

x = int(input("Digite quantos numeros deseja somar:  "))

while contador < x:
    numero = int(input("Digite num número: "))
    lista.append(numero)
    contador += 1


soma = sum(lista)
print(f"Os valores digitados somam o total de {soma}")





