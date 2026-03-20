#EX. 5: Calculadora de Média
#Conceitos: Listas, "sum()", "len()"
# Peça 4 notas ao usuário e calcule a média
# Mostre se o aluno foi aprovado (média >= 7) ou reprovado

print("Calculadora de Média")
notas = []
for i in range(4):
   nota = float(input(f"Digite a nota {i+1}: "))
   notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média do aluno é: {media:.2f}")

if media >= 7:
   print("O aluno foi aprovado.")
else:
   print("O aluno foi reprovado.")  