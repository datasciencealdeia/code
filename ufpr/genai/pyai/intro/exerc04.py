#EX. 4: Conversor de Temperatura
#Conceitos: Operações matemáticas, formatação de strings
# Converta Celsius para Fahrenheit: (C × 9/5) + 32
# Peça a temperatura em Celsius e mostre em Fahrenheit

print("Conversor de Temperatura")
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
