marcaCaneta = ['Faber-Castell', 'BIC', 'Uni-Ball', 'Crown']
corCaneta = ['Azul', 'Preto', 'Vermelho', 'Verde']
canetas = []
anot = []
cAnot = []


class Caneta:

    def __init__(self, marca, cor, tipo_ponta, tampa):
        self.marca = str(marca)
        self.cor = str(cor)
        self.tipo_ponta = float(tipo_ponta)
        self.tampa = bool(tampa)


def escolha_marca():
    while True:
        print("\n| SELECIONE A MARCA |")
        for i in range(len(marcaCaneta)):
            print(f"| {i + 1} - " + marcaCaneta[i])
        try:
            esc_mrc = int(input("| Escolha: "))
            return marcaCaneta[esc_mrc - 1]
        except:
            print("| Selecione uma opção válida!")
            continue


def escolha_cor():
    while True:
        print("\n| SELECIONE A COR |")
        for i in range(len(corCaneta)):
            print(f"| {i + 1} - " + corCaneta[i])
        try:
            esc_cor = int(input("| Escolha: "))
            return corCaneta[esc_cor - 1]
        except:
            print("| Selecione uma opção válida!")
            continue


def escolha_ponta():
    while True:
        esc_pnt = input("""\n|      PONTAS      |
| Escolha o valor da ponta entre 0.3 e 0.7
| Digite: """)
        try:
            if 0.3 <= float(esc_pnt) <= 0.7:
                return esc_pnt
        except:
            print("| Digite um valor válido!")
            continue


def escolha_tampa():
    while True:
      print("\n| Tampar ou destampar - OPÇÕES ", end="")
      listar_canetas()
      esc_cnt = input("| Escolha: ")
      if int(esc_cnt):
        esc_cnt = int(esc_cnt)
        if canetas[esc_cnt-1]:
            if canetas[esc_cnt-1].tampa:
                print("\n| A caneta está tampada!")
                esc_tmp = str(input("| Deseja destampar a caneta? [S/N]: ")).lower().strip()
                if esc_tmp[:1] == 's':
                    canetas[esc_cnt-1].tampa = False
                    print("\n| Caneta destampada!")
                elif esc_tmp[:1] == 'n':
                    print("\n| Voltando..")
                else:
                    print("\n| Selecione uma opção válida!")
                break

            else:
                print("\n| A caneta está destampada!")
                esc_tmp = str(input("| Deseja tampar a caneta? [S/N]: ")).lower().strip()
                if esc_tmp[:1] == 's':
                    canetas[esc_cnt-1].tampa = True
                    print("| Caneta tampada!")
                elif esc_tmp[:1] == 'n':
                    print("\n| Voltando..")
                else:
                    print("\n| Selecione uma opção válida!")
                break
      else:
        print("\n| Selecione uma opção válida!")
        continue


def excluir():
    while True:
        print("\n| Excluir caneta - OPÇÕES", end="")
        listar_canetas()
        esc_exc = input("| Escolha: ")

        try:
            esc_exc = int(esc_exc)

            if canetas[esc_exc-1]:
                cnt_esc = str(input(f"| Deseja excluir a caneta marca: {canetas[esc_exc-1].marca} | cor:"
                                    f" {canetas[esc_exc-1].cor}? [S/N]: ")).lower().strip()
                if cnt_esc[:1] == 's':
                    canetas.pop(esc_exc-1)
                    print("\n| Caneta excluida!")
                elif cnt_esc[:1] == 'n':
                    print("\n| Retornando..")
                else:
                    print("\n| Selecione uma opção válida!")
                break
            else:
                print("\n| Selecione uma opção válida!")
                continue

        except:
            print("\n| Selecione uma opção válida!")
            continue


def tampa(can):
    if can:
        return "Tampada"
    elif not can:
        return "Destampada"


def criar_caneta():
    caneta = Caneta(escolha_marca(), escolha_cor(), escolha_ponta(), True)
    canetas.append(caneta)
    del caneta


def listar_canetas(contador=1):
    print("\n|------CANETAS-----|")
    if len(canetas) > 0:
        for caneta in canetas:
            print(f"| CANETA {contador} = Marca: {caneta.marca} | Cor: {caneta.cor} | Ponta: {caneta.tipo_ponta} |"
                  , tampa(caneta.tampa))
            contador += 1
    else:
        print("\n| NENHUMA CANETA REGISTRADA |")


def consulta_anotacoes():
    print(anot[0])
    print(cAnot[0].marca, cAnot[0].cor)


def anotar():
    while True:
        print("\n| ANOTAR - escolha caneta - OPÇÕES", end="")
        listar_canetas()
        esc_ant = input("| Escolha: ")
        try:
            esc_ant = int(esc_ant)
            cAnot.append(canetas[esc_ant-1])
            anota = str(input("| Escreva: "))
            anot.append(anota)
            break
        except:
            print("\n| Selecione uma opção válida!")
            continue


def anotacoes():

    while True:
        anotMenu = input("""\n|----ANOTAÇÕES----|
| 1 - Consultar anotações
| 2 - Anotar
| 3 - Sair    
| Escolha: 
""")
        try:
            anotMenu = int(anotMenu)
            if anotMenu == 1:
                consulta_anotacoes()
                continue
            elif anotMenu == 2:
                anotar()
                continue
            elif anotMenu == 3:
                pass
            elif anotMenu == 4:
                pass
        except:
            print("\n| Selecione uma opção válida!")
            continue


def acoes_caneta():
    while True:
        acoesMenu = input("""\n|----AÇÕES NA CANETA ----|
| 1 - Tampar / Destampar
| 2 - Anotações
| 3 - Excluir caneta
| 4 - Sair
| Escolha: """)
        try:
            acoesMenu = int(acoesMenu)
            if acoesMenu == 1:
                escolha_tampa()
                continue

            elif acoesMenu == 2:
                anotacoes()
                continue

            elif acoesMenu == 3:
                excluir()
                continue

            elif acoesMenu == 4:
                print("\n| Retornando ao menu!")
                break

        except:
            print("\n| Selecione uma opção válida!")
            continue


while True:

    menu = input("""
|-------MENU--------| 
| 1 - Criar caneta
| 2 - Listar canetas
| 3 - Ações na caneta
| 4 - Sair
| Escolha: """)

    try:
        menu = int(menu)
        if menu == 1:
            criar_caneta()
            continue

        elif menu == 2:
            listar_canetas()
            continue

        elif menu == 3:
            acoes_caneta()
            continue

        elif menu == 4:
            print("\n| Finalizando..")
            break

        else:
            print("\n| Selecione uma opção válida!")
            continue

    except:
        print("\n| Selecione uma opção válida!")
        continue

