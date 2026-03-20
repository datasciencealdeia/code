# EX. 8: Contador de Vogais
# Conceitos: Strings, loops, condicionais
# Peça uma palavra ou frase e conte quantas vogais (a, e, i, o, u) ela tem
# Desafio: Conte também as consoantes

def contar_vogais_consoantes(texto):
    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    contador_vogais = 0
    contador_consoantes = 0
    
    for char in texto:
        if char in vogais:
            contador_vogais += 1
        elif char in consoantes:
            contador_consoantes += 1
            
    return contador_vogais, contador_consoantes

# Solicitar entrada do usuário
entrada = input("Digite uma palavra ou frase: ")
vogais, consoantes = contar_vogais_consoantes(entrada)
print(f"Número de vogais: {vogais}")
print(f"Número de consoantes: {consoantes}")

