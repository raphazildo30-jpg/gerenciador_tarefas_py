# menu de opçao se escolher sair do programa e um lower para transformar a escrita em minusculo
tarefas = []
while True:
    print("=-------Menu de Opçoes---------=")
    print("= 1. Adicionar tarefas =.")
    print("= 2. listar tarefas =.")
    print("= 3. Remover tarefas ")
    print("= 4. Sair ")

    # adicionado tarefas a lista
    opcao = input("ESCOLHA UMA OPÇAO:")

    # condição que adiciona tarefas se o user digitar 1
    if opcao == '1':
        tarefa = input("Digite uma Tarefa")
        tarefas.append(tarefa)
        print("Tarefa adicionada :", tarefa)
    # condiçao que o usuaruo Lista Tarefas que foram adicionadas
    elif opcao == '2':
        print("Lista de Tarefas :")
        for tarefa in tarefas:
            print("-", tarefa)
    # condiçao que Remove an Tarefa do usuario assim que ele digita e coloca o nome da Tarefa
    elif opcao == '3':
        print("Remove tarefas ")
        tarefa = input("Digite uma Tarefa a ser removida")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida", tarefa)
        else:
            print("Tarefa nao encontrada")

    # Sair opçao Invalida
    else:
        print("Opçao Invalida ")