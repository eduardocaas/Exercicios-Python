# Avaliação 02 individual
# Autor: Eduardo F. Castro

logins = []
senhas = []
funcionariosAumento = []
funcionarios = ['Pedro', 'Ana', 'Carlos', 'Maria', 'João']
salarios = [3470.00, 2200.00, 3970.34, 7450.23, 5677.33]
con = ''
ver = ''

print("| Avaliação 02 - Individual | Autor: Eduardo F. Castro\n")

while True:
    opcoes = ['Lista de Funcionários', 'Cadastrar Login e Senha', 'Aumento de 10%', 'Relatório', 'Cadastrar Funcionário', 'Sair']
    print("-" * 11 + "| MENU |" + "-" * 11)
    for i in range(len(opcoes)):
        print(f"{[i + 1]} -", opcoes[i])
    opcao = input("| Escolha: ")

    try:
        opcao = int(opcao)
        if opcao <= 5:
            pass
        else:
            print("\n---| DIGITE UMA OPÇÃO VÁLIDA! |---\n")
            pass
    except:
        print("\n---| DIGITE UMA OPÇÃO VÁLIDA! |---\n")
        continue
    
    if opcao == 1:
        print("\n---| LISTA DE FUNCIONÁRIOS |---")
        for f in range(len(funcionarios)):
            print(f"| Funcionário {f+1}: {funcionarios[f]}")
        while True:
            del con
            con = str(input("\n| Deseja voltar ao menu? [S / N]: "))
            if con in 'sS':
                print("\n")
                break
            if con in 'nN':
                input()
            else:
                print("\n---| OPÇÃO INVÁLIDA! |---\n")
                input()

    if opcao == 2:
        print("\n---| CADASTRO DE LOGIN E SENHA |---  Dica: só vai aceitar nomes da lista funcionários ex: 'Pedro'")
        while True:
            nomeLogin = str(input("| Digite o login a ser cadastrado: "))

            if nomeLogin in logins:
                print("\n| SEU NOME JÁ ESTÁ CADASTRADO NO SISTEMA! \n")
                continue
            elif nomeLogin in funcionarios:
                senhaLogin = input("| Digite a senha (mínimo 6 caracteres): ")
                if len(senhaLogin) <= 5:
                    print("| DIGITE UMA SENHA COM MAIS CARACTERES! \n")
                else:
                    print(f"\n| USUÁRIO CADASTRADO COM SUCESSO! | Usuário: {nomeLogin} | Senha: {senhaLogin}")
                    logins.append(nomeLogin)
                    senhas.append(senhaLogin)

                    del con
                    con = str(input("\n| Deseja cadastrar outro login? [S / N]: "))
                    if con in 'sS':
                        continue
                    if con in 'nN':
                        print("\n")
                        break
                    else:
                        print("\n---| OPÇÃO INVÁLIDA! |---\n")
                        break

            else:
                print("| SEU NOME NÃO CONSTA NO GRUPO DE FUNCIONÁRIOS!\n")
                continue

    if opcao == 3:
        print("\n---| AUMENTO DE 10% |---")
        while True:
            del ver
            ver = str(input("| Deseja se logar? [S / N]: "))
            if ver in 'sS':
                login = input("Digite seu login: ")
                senha = input("Digite sua senha: ")
                if login in logins:
                    if logins[logins.index(login)] == login:
                        if senha in senhas:
                            if senhas[senhas.index(senha)] == senha:
                                for x in range(len(funcionarios)):
                                    if salarios[x] < (sum(salarios) / len(salarios)):
                                        salarios[x] = salarios[x] * 1.1
                                        funcionariosAumento.append(funcionarios[x])

                                print("| FUNCIONÁRIOS QUE RECEBERAM AUMENTO SALARIAL DE 10%: ")
                                print("| Funcionários: ", end="")
                                for y in range(len(funcionariosAumento)):
                                    print(f"{funcionariosAumento[y]}", end=" | ")

                                funcionariosAumento.clear()  # para não repetir os nomes

                                del con
                                con = str(input("\n\n| Deseja voltar ao menu? [S / N]: "))
                                if con in 'sS':
                                    print("\n")
                                    break
                                if con in 'nN':
                                    continue
                                else:
                                    print("\n---| OPÇÃO INVÁLIDA! |---\n")
                                    break

                        else:
                            print("| LOGIN INVÁLIDO!")
                            continue
                else:
                    print("| LOGIN INVÁLIDO!")
                    continue
            if ver in 'nN':
                print("\n---| RETORNANDO AO MENU! |---\n")
                break
            else:
                print("\n---| OPÇÃO INVÁLIDA! |---\n")
                continue

    if opcao == 4:
        while True:
            del ver
            ver = str(input("| Deseja se logar? [S / N]: "))
            if ver in 'sS':
                login = input("| Digite seu login: ")
                senha = input("| Digite sua senha: ")

                if login in logins:
                    if logins[logins.index(login)] == login:
                        if senha in senhas:
                            if senhas[senhas.index(senha)] == senha:
                                print("\n    --------------------------")
                                print("    |   FOLHA DE PAGAMENTO   |")
                                print("    --------------------------")
                                print("    |  EQUIPE    |  SALÁRIOS |")
                                print("    --------------------------")
                                for i in range(len(funcionarios)):
                                    print(f"    |  {funcionarios[i]}" + " " * (10-len(funcionarios[i])) + "|" + " " * 2
                                          + "%.2f  |" % salarios[i])
                                print("    --------------------------\n")

                                del con
                                con = str(input("| Deseja voltar ao menu? [S / N]: "))
                                if con in 'sS':
                                    print("\n")
                                    break
                                if con in 'nN':
                                    continue
                                else:
                                    print("\n---| OPÇÃO INVÁLIDA! |---\n")
                                    break

                        else:
                            print("| SENHA INVÁLIDA!")
                            continue
                else:
                    print("| NOME INVÁLIDO!")
                    continue

            if ver in 'nN':
                print("\n---| RETORNANDO AO MENU! |---\n")
                break
            else:
                print("\n---| OPÇÃO INVÁLIDA! |---\n")
                continue

    if opcao == 5:
        print("\n---| CADASTRO DE FUNCIONÁRIO |---")
        while True:
            nomeCadastro = input("| Digite o nome a ser cadastrado: ")

            if any(numero.isdigit() for numero in nomeCadastro):
                print("\n| DIGITE UM NOME VÁLIDO! \n")
                continue
            else:
                funcionarios.append(nomeCadastro.capitalize())
                break

        while True:
            salarioCadastro = input("| Digite o salário a ser cadastrado: ")
            if type(salarioCadastro) == str:
                try:
                    salarios.append(float(salarioCadastro))
                    print(f"\n| FUNCIONÁRIO CADASTRADO COM SUCESSO! |"
                          f" Nome: {nomeCadastro.capitalize()} | Salário: {salarioCadastro}\n")

                    del con
                    con = str(input("\n\n| Deseja cadastrar outro login? [S / N]: "))
                    if con in 'sS':
                        print("\n")
                        break
                    if con in 'nN':
                        continue
                    else:
                        print("\n---| OPÇÃO INVÁLIDA! |---\n")
                        break

                except:
                    print("\n| DIGITE UM SALÁRIO VÁLIDO!\n")
                    continue

    if opcao == 6:
        print("\n---| PROGRAMA FINALIZADO |---")
        break
