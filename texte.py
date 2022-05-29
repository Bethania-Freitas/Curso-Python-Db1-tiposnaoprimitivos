from collections import Counter
string2 = ['abc', 'xyz', 'aba', '1221']
contador = 0
for str1 in range(len(string2)):
    if string2[str1][0] == string2[str1][-1] and len(string2) > 2:
        contador += 1
print(f'A(s) quantidade(s) de string(s) pedida(s) é(são) {contador}.')