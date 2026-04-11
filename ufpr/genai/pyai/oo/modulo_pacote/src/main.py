from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

try:
    p1 = Pessoa("João da Silva", 12341115678909)
    p2 = Pessoa("Maria Oliveira", 98765432100)
except "CPFInvalidoException" as e:
    print(f"Erro ao criar pessoa: {e}")

d1 = Disciplina("Python para IA", 60, p1)
d2 = Disciplina("Linguagem C")
d1.adicionar_conteudo_ministrado("Getters e Setters", 1)
d1.adicionar_conteudo_ministrado("Classes", 2)
d1.adicionar_conteudo_ministrado("Modificadores de Acesso", 1)

d2.adicionar_conteudo_ministrado("Tipo de Dados", 1)
d2.adicionar_conteudo_ministrado("Ponteiros", 3)
d2.adicionar_conteudo_ministrado("Estrutura Condicional", 4)

d1.exibir_informacoes()
d2.exibir_informacoes()

p1 = Pessoa("João", 33333333333)
p2 = Pessoa("Maria", 33333333333)

if p1 == p2:
    print("Pessoas Iguais")
else:
    print("Pessoas Diferentes")

