# Tarefa 03 - Lógica de programação
# Seu nome Aqui: Eduardo F. Castro.
produtosNome = ['Arroz' , 'Feijão' , 'Leite' , 'Ovos' , 'Biscoito'] # adicionei opção de nome
produtosCod = [1001 , 1324 , 6548 , 2987 , 7623]
produtosVal = [5.32 , 6.45 , 2.37 , 5.32 , 6.45]
contador = 10

nomeCompra = []
codCompra = []
qntCompra = []
somaCompra = []

while True:
    print("-" * 19)
    escolha = input("|     MENU        |\n| [1] - TABELA    |\n| [2] - CAIXA     |\n| [3] - ADICIONAR |\n| [4] - SAIR "
                    "     |\n| ESCOLHA: ")
    try:
        escolha = int(escolha)
    except:
        print("\n| DIGITE UMA OPÇÃO VÁLIDA!\n")
        continue

    if escolha == 1:
        print("\n| " + "-"*7 + " TABELA DE PRODUTOS " + "-"*7 + " |" + "\n|     NOME     | CÓDIGO | PREÇO UNI. |")
        for x in range(len(produtosNome)):
            print("|    " + produtosNome[x].ljust(10) + "|  " + str(produtosCod[x]) + "  |    " + str(produtosVal[x]) + "    |")
        print("-" * 38 + "\n")

    if escolha == 2:
        nome = str(input("| Nome do cliente: "))
        while True:
            cod_nome = input("| ['fim' - parar] | Digite o código ou nome do produto: ") # pode ser usado o nome ou cod
            if cod_nome == 'fim':
                print("\n| NOME: ", nome.capitalize())
                print("|  PRODUTO  |  QNTD  |  PREÇO  |")
                print("-"*32)
                for i in range(len(somaCompra)):
                    print("|" + (str(codCompra[i])).center(11), end="")
                    print("|" + (str(qntCompra[i])).center(8), end="")
                    print("|" + (str(somaCompra[i])).center(9) + "|", end="")
                    print()
                print("-" * 32)
                print("| VALOR TOTAL: %.2f" % sum(somaCompra))
                print("-" * 32)
                print("\n")
                somaCompra.clear() # limpar lista
            if cod_nome != 'fim':
                try:  # se for um numero digitado cai como código
                    cod_nome = int(cod_nome)
                    if cod_nome in produtosCod:
                        codCompra.append(cod_nome)
                        prod = int(input("| Digite a quantidade de produtos: "))
                        qntCompra.append(prod)
                        soma = prod * produtosVal[produtosCod.index(cod_nome)] # posicao do valor do prod na lista
                        somaCompra.append(soma)
                    else:
                        print("| DIGITE UM CÓDIGO VÁLIDO! ")
                except: # reconhece como string 'nome'
                    if cod_nome.capitalize() in produtosNome:
                        codCompra.append(cod_nome)
                        prod = int(input("| Digite a quantidade de produtos: "))
                        qntCompra.append(prod)
                        soma = prod * produtosVal[produtosNome.index(cod_nome.capitalize())]  # posicao do valor do prod na lista
                        somaCompra.append(soma)
                    else:
                        print("| DIGITE UM NOME DE PRODUTO VÁLIDO! ")

    if escolha == 3:
        print("\n| ADICIONAR PRODUTO |")
        while True:
            esc = input("| [1] - Adicionar por nome \n| [2] - Adicionar por código\n| [3] - Sair\n| ESCOLHA: ")
            try:
                esc = int(esc)
                if esc == 1:
                    nome = input("\n| Digite o nome do produto: ")
                    try:
                        nome = int(nome)
                        print("| Digite um nome válido!")
                        continue
                    except:
                        if nome.capitalize() not in produtosNome:
                            valor = input("| Digite o valor: ")
                            try:
                                valor = float(valor)
                                produtosVal.append(valor)
                                produtosCod.append(1000+contador) # pra nao ficar o codigo vago
                                produtosNome.append(nome)
                                contador += 1 # pra nao repetir o codigo gerados
                                print("\n| Produto adicionado com sucesso!\n")
                                break
                            except:
                                print("| Valor inválido!")
                                continue
                        if nome.capitalize() in produtosNome:
                            print("| Produto já listado!")
                            continue

                if esc == 2:
                    while True:
                        codigo = input("\n| Digite o código do produto [4 digitos]: ")
                        try:
                            codigo = int(codigo)
                            if len(str(codigo)) == 4:
                                if codigo not in produtosCod:
                                    valor = input("| Digite o valor do produto: ")
                                    try:
                                        valor = float(valor)
                                        produtosVal.append(valor)
                                        produtosCod.append(codigo)
                                        produtosNome.append("ADC" + str(contador))
                                        contador += 1
                                        print("\n| Produto adicionado com sucesso!\n")
                                        break
                                    except:
                                        print("| Digite um valor válido!")
                                if codigo in produtosCod:
                                    print("| Código já listado!")
                                    continue
                            if len(str(codigo)) != 4:
                                print("| Digite apenas 4 digitos!")
                                continue


                        except:
                            print("| Digite um código válido!")
                if esc == 3:
                    print("\n| VOLTANDO AO MENU! \n")
                    break
                if esc != 1 or esc != 2 or esc != 3:
                    continue
            except:
                print("| Digite uma opção válida!")
                continue

    if escolha == 4:
        print("\n| FIM!")
        break