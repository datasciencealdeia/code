from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

p1 = Pessoa("João da Silva", 12345678900)
d1 = Disciplina("Python para IA", 60, p1)
d2 = Disciplina("Linguagem C", 60)
d1.adicionar_conteudo_ministrado("Getters e Setters", 1)
d1.adicionar_conteudo_ministrado("Classes", 2)
d1.adicionar_conteudo_ministrado("Modificadores de Acesso", 1)

d2.adicionar_conteudo_ministrado("Tipo de Dados", 1)
d2.adicionar_conteudo_ministrado("Ponteiros", 3)
d2.adicionar_conteudo_ministrado("Estrutura Condicional", 4)

d1.exibir_informacoes()
d2.exibir_informacoes()

