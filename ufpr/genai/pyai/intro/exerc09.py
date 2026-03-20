# EX. 9: Jogo da Adivinhação
# Conceitos: Random, loops, condicionais
# Gere um número aleatório entre 1 e 100
# Peça para o usuário adivinhar, dando dicas de "maior" ou "menor"
#  O jogo acaba quando o usuário acertar

import random
def jogo_adivinhacao():
   numero_secreto = random.randint(1, 100)
   tentativas = 0
   acertou = False

   while not acertou:
      palpite = int(input("Adivinhe o número entre 1 e 100: "))
      tentativas += 1
      
      if palpite < numero_secreto:
         print("Tente um número maior!")
      elif palpite > numero_secreto:
         print("Tente um número menor!")
      else:
         acertou = True
         print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

jogo_adivinhacao()