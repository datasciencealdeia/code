'''
4. Remoção de espaços extras
   Escreva uma função que remova espaços desnecessários: espaços no início/fim e múltiplos espaços entre palavras 
   (deixe apenas um).
   Exemplo: `" Olá mundo da IA "` → `"Olá mundo da IA"`
'''

def remover_espacos_extras(texto):
    # Remove espaços no início e no fim, e reduz múltiplos espaços a um único espaço
    return ' '.join(texto.split())

# Exemplo de uso
texto = input("Digite uma string: ")
resultado = remover_espacos_extras(texto)
print(f'Resultado: "{resultado}"')