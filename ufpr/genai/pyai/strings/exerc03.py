'''
3. Contagem de vogais e consoantes
   Dada uma string, conte quantas vogais (a, e, i, o, u) e quantas consoantes ela possui. Ignore maiúsculas/minúsculas.
   Exemplo: `"GenAI"` → Vogais: 3, Consoantes: 2
'''
def contar_vogais_consoantes(texto):
    vogais = 'aeiouAEIOU'
    contagem_vogais = 0
    contagem_consoantes = 0

    for char in texto:
        if char.isalpha():  # Verifica se é uma letra
            if char in vogais:
                contagem_vogais += 1
            else:
                contagem_consoantes += 1

    return contagem_vogais, contagem_consoantes

# Exemplo de uso
texto = input("Digite uma string: ")
vogais, consoantes = contar_vogais_consoantes(texto)
print(f'Vogais: {vogais}, Consoantes: {consoantes}')

