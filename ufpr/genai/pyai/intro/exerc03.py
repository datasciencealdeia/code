#EX. 3: Par ou Ímpar
#Conceitos: Operador "%" (módulo), condicionais "if/else"
#Peça um número ao usuário e diga se ele é par ou ímpar

print("Verificador de Par ou Ímpar")
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

