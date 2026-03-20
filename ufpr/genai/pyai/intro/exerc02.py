#EX. 2: Calculadora de Soma
#Conceitos: Tipos numéricos, conversão de tipos
# Peça dois números ao usuário e mostre a soma deles
# Desafio: Mostre também a subtração, multiplicação e divisão

print("Calculadora de Soma")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

print(f"A soma é: {soma:.2f}")
print(f"A subtração é: {subtracao:.2f}")
print(f"A multiplicação é: {multiplicacao:.2f}")
print(f"A divisão é: {divisao}")
