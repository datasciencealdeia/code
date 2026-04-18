'''
2. Inversão de string
   Crie uma função que inverta uma string sem usar fatiamento `[::-1]` (use um loop).
   Exemplo: `"Python"` → `"nohtyP"`
'''

invertido = ''
palavra = input("Entre com uma palavra: ")

for i in range(len(palavra)-1, -1, -1):
   invertido = invertido+palavra[i]

print('"{}"'.format(palavra) + "→ '{}'".format(invertido))