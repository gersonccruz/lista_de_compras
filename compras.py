def lista_de_compras():
    produtos = []
    proximo_id = 1
    while True:
        print("********************")
        print("--Lista de compras--")
        print("********************")
        print()
        print("1. Adicionar produtos")
        print("2. Remover produtos")
        print("3. Pesquisar produtos")
        print("4. Sair do sistema")

        escolha = input("Digite sua escolha: ")

        if escolha == '4':
            print("Obrigado por usar o sistema!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção invalida! tente novamente")
            continue



        unidades_de_medida = [
            "Quilograma",
            "Grama",
            "Litro",
            "Mililitro",
            "Metro",
            "Centímetro"
        ]

        if escolha == '1':
            nome = input("Qual o nome do produto: ")

            for i, unidade in enumerate(unidades_de_medida, start=1):
                print(f"{i} - {unidade}")
            unidade_escolhida = unidades_de_medida[int(input("Qual o numero da unidade do produto: "))]

            quantidade = int(input("Qual a quantidade do produto: "))
            descricao_do_produto = input("Descreva o produto: ")

            produto = {
                "id": proximo_id,
                "nome": nome,
                "unidade": unidade_escolhida,
                "quantidade": quantidade,
                "descricao": descricao_do_produto
            }

            produtos.append(produto)
            proximo_id += 1

            print()
            print("--> Produto adicionado com sucesso!")
            print()

        if escolha == '2':
            id_procurado = int(input("Digite o id para remover: "))

            removido = False
            for p in produtos:
                if p["id"] == id_procurado:
                    produtos.remove(p)
                    removido = True
                    break

            if removido:
                print("Produto removido com sucesso!")
            else:
                print("Produto não escontrado!")









lista_de_compras()
