#Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais.

lista = []
lista2 = []
contador = 0


x = int(input("Digite quantos itens quer colocar na lista: "))
while contador < x:
    item = (input("Digite um item: "))
    contador += 1
    lista.append(item)

print(f"Sua lista: {lista}")

lista2 = [string for string in lista if len(string) > 2 if string[0]==string[-1]]
print(f"Os itens com mais de caracteres e cuja primeira e ultima letra são iguais são {lista2}")


