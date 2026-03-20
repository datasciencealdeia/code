# EX. 10: Lista de Compras
#Conceitos: Listas, loops, manipulação de listas
# Crie um programa que:
# 1. Permita adicionar itens à lista de compras
# 2. Permita remover itens
# 3. Mostre a lista atual
# 4. Encerre o programa

def lista_compras():
    compras = []
    
    while True:
        print("\nLista de Compras:")
        for idx, item in enumerate(compras, start=1):
            print(f"{idx}. {item}")
        
        print("\nOpções:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Encerrar programa")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        if escolha == '1':
            item = input("Digite o item para adicionar: ")
            compras.append(item)
            print(f"{item} adicionado à lista.")
        
        elif escolha == '2':
            item = input("Digite o item para remover: ")
            if item in compras:
                compras.remove(item)
                print(f"{item} removido da lista.")
            else:
                print(f"{item} não encontrado na lista.")
        
        elif escolha == '3':
            print("Encerrando programa. Lista final de compras:")
            for idx, item in enumerate(compras, start=1):
                print(f"{idx}. {item}")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

lista_compras()
