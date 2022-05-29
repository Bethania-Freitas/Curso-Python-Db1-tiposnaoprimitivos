#Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com'  Resultado Esperado: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} )

from collections import Counter

string = input("Digite a frase que deseja saber os caracteres: ")
contador_strings = dict(Counter(string))

print(contador_strings)
