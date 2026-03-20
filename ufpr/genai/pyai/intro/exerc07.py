# EX. 7: Números Primos
# Conceitos: Loops "while", lógica matemática
# Peça um número e diga se ele é primo ou não
# Um número primo só é divisível por 1 e por ele mesmo

print("Verificador de Números Primos")
numero = int(input("Digite um número: "))
if numero < 2:
   print(f"O número {numero} não é primo.")
else:
   primo = True
   divisor = 2
   while divisor < numero:
       if numero % divisor == 0:
           primo = False
           break
       divisor += 1

   if primo:
       print(f"O número {numero} é primo.")
   else:
       print(f"O número {numero} não é primo.")