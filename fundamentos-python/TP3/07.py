# Escreva um programa em Python que realiza operações de inclusão e remoção em listas.
# Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)

# - Mostrar lista;
# - Incluir elemento;
# - Remover elemento;
# - Apagar todos os elementos da lista.

# Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista.
# Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído.
# Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido.
# E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

operacoes_permitidas = ('a', 'b', 'c', 'd', 'sair')
itens = []

def menu():
    while True:

        print('Operações disponíveis: ', "\n")
        print('► Mostrar lista; (A) ')
        print('► Incluir elemento; (B) ')
        print('► Remover elemento; (C) ')
        print('► Apagar todos os elementos da lista; (D) ', "\n")
        print('► Sair; (sair) ', "\n")

        operacao = input(f"Qual operação deseja fazer? ").lower()

        if operacao not in operacoes_permitidas:
            print('Operação não disponível, tente novamente.')
        else:
            return operacao
            break

def listar():
    print("Itens Aramazenados na Lista: ", "\n")
    print("\n".join(itens))
    print("\n ----------------------- \n")

def adicionar():
    while True:
        data = input(f"Informe o item que quer adicionar: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            itens.append(data)
            print("-----------------------\n", "✔ Item adicionado com sucesso.", "\n-----------------------\n")
            break

def remover():
    while True:
        data = input(f"Informe o nome do item que será deletado: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            if data in itens:
                itens.remove(data)
                print("-----------------------\n", "✔ Item removido com sucesso.", "\n-----------------------\n")
            else:
                print("-----------------------\n", "✘ O item informado não existe na lista.", "\n-----------------------\n")

            break

def limpar():
    itens.clear()
    print("-----------------------\n", "✔ A lista foi apagada com sucesso.", "\n-----------------------\n")

while True:
    operacao = menu()

    print("\n -----------------------\n")

    if operacao == 'sair':
        break
    elif operacao == 'a':
        listar()
    elif operacao == 'b':
        adicionar()
    elif operacao == 'c':
        remover()
    elif operacao == 'd':
        limpar()
