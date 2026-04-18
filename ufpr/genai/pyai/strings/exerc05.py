'''
5. Verificador de palíndromo
   Verifique se uma string é um palíndromo (ignorando maiúsculas, acentos e espaços).
   Exemplo: `"A man a plan a canal panama"` → `True`
'''
import unicodedata
def remover_acentos(texto):
    # Remove acentos usando unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def verificar_palindromo(texto):
    # Remove acentos, espaços e converte para minúsculas
    texto = remover_acentos(texto)
    texto = texto.replace(" ", "").lower()
    
    # Verifica se é um palíndromo
    return texto == texto[::-1]

# Exemplo de uso
texto = input("Digite uma string: ")
if verificar_palindromo(texto):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")