estoque = {} #DECLARE estoque COMO DICIONÁRIO
opcao = int() #DECLARE opcao COMO INTEIRO

#int < , #Inicializa a variável de controle do loop
while opcao != 3: #ENQUANTO opcao <> 3 FAÇA
    print("MENU: ") #EXIBA "MENU: "
    print("1 - Adicionar Produto") #EXIBA "1 - Adicionar Produto"
    print("2 - Consultar Produto") #EXIBA "2 - Consultar Produto"
    print("3 - Sair") #EXIBA "3 - Sair"
    opcao = int(input("Escolha uma opção: ")) #LEIA opcao

    if (opcao == 1): #SE opcao = 1 ENTÃO
        nome_produto = input("Digite o nome do produto: ") #EXIBA "Digite o nome do produto: "
        quantidade = int(input("Digite a quantidade: ")) #EXIBA "Digite a quantidade: "

        if (nome_produto in estoque): #SE nome_produto ESTÁ EM estoque ENTÃO
            estoque[nome_produto] += quantidade #estoque[nome_produto] ← estoque[nome_produto] + quantidade
            print("Quantidade atualizada!") #EXIBA "Quantidade atualizada!"
        else:
            estoque[nome_produto] = quantidade #estoque[nome_produto] ← quantidade
            print("Produto adicionado!") #EXIBA "Produto adicionado!"

    elif (opcao == 2): #SENÃO SE opcao = 2 ENTÃO
        nome_produto = input("Digite o nome do produto para consulta: ") #EXIBA "Digite o nome do produto para consulta: "
    
        if (nome_produto in estoque): #SE nome_produto ESTÁ EM estoque ENTÃO
            print("Quantidade disponível:", estoque[nome_produto]) #EXIBA "Quantidade disponível: ", estoque[nome_produto]
        else:
            print("Produto não encontrado.") #EXIBA "Produto não encontrado."

    elif (opcao == 3): #SENÃO SE opcao = 3 ENTÃO
       print("Saindo do sistema...") #EXIBA "Saindo do sistema..."
    else:
        print("Opção inválida! Tente novamente.") #EXIBA "Opção inválida! Tente novamente."