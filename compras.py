def lista_de_compras():
    produtos = []
    proximo_id = 1

    while True:
        print("********************")
        print("--Lista de compras simples--")
        for p in produtos:
            print("------------------------------")
            print(f"ID: {p['id']}")
            print(f"Nome: {p['nome']}")
            print(f"Unidade: {p['unidade']}")
            print(f"Quantidade: {p['quantidade']}")
            print(f"Descricao: {p['descricao']}")
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

        if escolha == '3':

            termo = input("Digite o termo que deseja procurar: ").lower()

            encontrados = []

            for p in produtos:
                if termo in p["nome"].lower():
                    encontrados.append(p)

            if encontrados:
                print("Produto(s) encontrado(s) com sucesso!\n")
                for p in encontrados:
                    print(f"ID: {p['id']}")
                    print(f"Nome: {p['nome']}")
                    print(f"Quantidade: {p['quantidade']}")
                    print()
                print(f"Total de produtos encontrados: {len(encontrados)}")
            else:
                print("Produto(s) não encontrado(s)!")


lista_de_compras()
