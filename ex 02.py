#Escreva um programa que multiplique todos os itens de uma lista.

lista = []
contador = 0

x = int(input("Digite os numeros para colocar na lista:  "))

while contador < x:
    numero = int(input("Digite num número: "))
    lista.append(numero)
    contador += 1

y = int(input("Digite por qual numero gostaria de multiplicar os numeros: "))
lista2 = [numero*y for numero in lista]

print(f"Sua lista que era de {lista}, foi multiplicada por {y} e agora valem {lista2}")


