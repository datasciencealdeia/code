print ('Fórmula de Bhaskara')

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    
    raiz = raiz + 0.0 # Garantir que a raiz seja um número de ponto flutuante de valor ZERO, para evitar a representação de -0.00
    
    print(f"A equação possui uma raiz real: {raiz:.2f}")
else:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)

    raiz1 = raiz1 + 0.0 # Garantir que a raiz seja um número de ponto flutuante de valor ZERO, para evitar a representação de -0.00
    raiz2 = raiz2 + 0.0 # Garantir que a raiz seja um número de ponto flutuante de valor ZERO, para evitar a representação de -0.00

    print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")   