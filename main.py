produtos = {}
id_produto = 1

#Menu inicial
def menu_inicial():
    print ('\n===== STOCKPILOT =====\n'
           '1 - Cadastrar produtos\n'
           '2 - Listar produtos\n'
           '3 - Buscar produtos\n'
           '4 - Atualizar produtos\n'
           '5 - Remover produtos\n'
           '6 - Sair\n')



#Cadastrar produtos
def cadastrar_produtos():
    global id_produto
    print ('\n===== CADASTRAR PRODUTOS =====')
    nome_produto = input ('Digite o nome do produto: ').strip().title()
    if nome_produto.replace(' ','').isalnum():
        try:
            valor_produto = float ( input ('Digite o valor do produto: '))
            if valor_produto >0:
                quantidade_produto = int ( input ('Digite a quantidade : '))
                if quantidade_produto >0:
                    categoria_produto = input ('Digite a categoria do produto: ').strip().title()
                    if categoria_produto.replace (' ','').isalpha():
                        produto={'id':id_produto,
                                 'nome':nome_produto,
                                 'valor':valor_produto,
                                 'quantidade':quantidade_produto,
                                 'categoria':categoria_produto,
                                 }
                        produtos[id_produto] = produto
                        print ('Produto cadastrado com sucesso!\n\n'
                               f'ID: {id_produto}\n'
                               f'Nome: {produto["nome"]}\n'
                               f'Valor: {produto["valor"]}\n'
                               f'Quantidade: {produto["quantidade"]}\n'
                               f'Categoria: {produto["categoria"]}\n'
                               '----------\n'
                               )
                        id_produto += 1
                    else:
                        print ('Categoria inválida.')

                else:
                    print ('Quantidade inválida.')
            else:
                print('Valor inválido.')

        except ValueError:
            print ('Valor inválido.')
    else:
        print ('Nome inválido.')

def listar_produtos():
    print ('\n===== LISTAR PRODUTOS =====\n')
    if not produtos:
        print ('Você não possue produtos cadastrados.')
        return

    for id_prod, produto in produtos.items():
        print (f'ID: {id_prod}\n'
        f'Nome: {produto["nome"]}\n'
        f'Valor: {produto["valor"]}\n'
        f'Quantidade: {produto["quantidade"]}\n'
        f'Categoria: {produto["categoria"]}\n'
        '----------\n'
        )

def buscar_produtos():
    print ('\n===== BUSCAR PRODUTOS =====\n')
    try:
        id_busca = (int (input ('Digite o ID do produto: ')))
        if id_busca not in produtos:
            print ('\nProduto não encontrado')
            return

        produto = produtos[id_busca]
        print ('\nProduto encontrado!\n\n'
                f'ID: {id_busca}\n'
                f'Nome: {produto["nome"]}\n'
                f'Valor: {produto["valor"]}\n'
                f'Quantidade: {produto["quantidade"]}\n'
                f'Categoria: {produto["categoria"]}\n'
             )
    except ValueError:
        print ('ID inválido.')

def atualizar_produtos():
    print ('\n===== ATUALIZAR PRODUTOS =====\n')
    try:
        id_busca = (int (input ('Digite o ID do produto: ')))
        if id_busca not in produtos:
            print('\nProduto não encontrado')
            return

        produto = produtos[id_busca]
        print('\nProduto encontrado!\n\n'
            f'ID: {id_busca}\n'
            f'Nome: {produto["nome"]}\n'
            f'Valor: {produto["valor"]}\n'
            f'Quantidade: {produto["quantidade"]}\n'
            f'Categoria: {produto["categoria"]}\n'
            )
        opcao = (input ('O que deseja atualizar?: ')).strip().title()
        if opcao not in ("Nome", "Valor", "Quantidade", "Categoria"):
            print ('Opção inválida.')
            return

        if opcao == "Nome":
            novo_nome = (input ('Digite o novo nome do produto: ')).strip().title()
            if novo_nome.replace(' ','').isalnum():
                produto["nome"] = novo_nome
                print ('Nome atualizado com sucesso.\n')
                print (f'ID: {id_busca}\n'
                      f'Nome: {produto["nome"]}\n'
                      f'Valor: {produto["valor"]}\n'
                      f'Quantidade: {produto["quantidade"]}\n'
                      f'Categoria: {produto["categoria"]}\n'
                      )

        elif opcao == "Valor":
            try:
                novo_valor = (float (input ('Digite o novo valor do produto: ')))
                if novo_valor >=0:
                    produto["valor"] = novo_valor
                    print ('Valor atualizado com sucesso.\n')
                    print (f'ID: {id_busca}\n'
                          f'Nome: {produto["nome"]}\n'
                          f'Valor: {produto["valor"]}\n'
                          f'Quantidade: {produto["quantidade"]}\n'
                          f'Categoria: {produto["categoria"]}\n'
                          )
            except ValueError:
                print ('Valor inválido.')

        elif opcao == "Quantidade":
            try:
                nova_quantidade = (int(input('Digite a nova quantidade do produto: ')))
                if nova_quantidade >=0:
                    produto["quantidade"] = nova_quantidade
                    print ('Quantidade atualizada com sucesso.\n')
                    print (f'ID: {id_busca}\n'
                          f'Nome: {produto["nome"]}\n'
                          f'Valor: {produto["valor"]}\n'
                          f'Quantidade: {produto["quantidade"]}\n'
                          f'Categoria: {produto["categoria"]}\n'
                          )
            except ValueError:
                print ('Quantidade inválida.')

        elif opcao == "Categoria":
            nova_categoria = (input('Digite a nova categoria do produto: ')).strip().title()
            if nova_categoria.replace(' ','').isalpha():
                produto["categoria"] = nova_categoria
                print ('Categoria atualizada com sucesso.\n')
                print (f'ID: {id_busca}\n'
                      f'Nome: {produto["nome"]}\n'
                      f'Valor: {produto["valor"]}\n'
                      f'Quantidade: {produto["quantidade"]}\n'
                      f'Categoria: {produto["categoria"]}\n'
                      )
    except ValueError:
        print ('ID inválido.')


def remover_produtos():
    print ('\n===== REMOVER PRODUTOS =====\n')
    try:
        id_remover = (int (input ('Digite o ID do produto: ')))
        if id_remover not in produtos:
            print('\nProduto não encontrado')
            return

        produto = produtos[id_remover]
        print ('\nProduto encontrado!\n\n'
            f'ID: {id_remover}\n'
            f'Nome: {produto["nome"]}\n'
            f'Valor: {produto["valor"]}\n'
            f'Quantidade: {produto["quantidade"]}\n'
            f'Categoria: {produto["categoria"]}\n'
            )
        opcao_remover = input (f'Tem certeza que deseja remover o produto ({produto["nome"]}) S/N?').strip().title()
        if opcao_remover not in ('S','Sim'):
            print ('Produto NÃO removido.\n')
            return

        elif opcao_remover in ('S','Sim'):
            del produtos[id_remover]
            print ('\nProduto removido com sucesso.\n')

    except ValueError:
        print ('ID inválido.')





while True:
    menu_inicial()
    try:
        opcao_menu = int(input('Digite a opção desejada: '))
        if opcao_menu not in (1, 2, 3, 4, 5, 6):
            print('Opção inválida.')
            continue

    except ValueError:
        print ('Opção inválida.')
        continue

    if opcao_menu == 1:
        cadastrar_produtos()
    elif opcao_menu == 2:
        listar_produtos()
    elif opcao_menu == 3:
        buscar_produtos()
    elif opcao_menu == 4:
        atualizar_produtos()
    elif opcao_menu == 5:
         remover_produtos()