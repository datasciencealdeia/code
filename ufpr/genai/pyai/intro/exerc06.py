# EX. 6: Tabuada
# Conceitos: Loops "for", range
# Peça um número e mostre a tabuada dele (1 a 10)
# Exemplo:
# 5 x 1 = 5
# 5 x 2 = 10 ...

print("Tabuada")
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

524
