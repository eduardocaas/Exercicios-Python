import time

class Porta:

    def __init__(self, largura=None):
        self.__cor = None
        self.__altura = 210
        self.__largura = largura
        self.__aberta = False


    def cores(self):
        escC = int(input("\nSelecione a cor: \n[1] - Vermelho \n[2] - Branco \n[3] - Amarelo \n[ ] - Escolha: "))
        if escC == 1:
            self.__cor = "Vermelho"
        elif escC == 2:
            self.__cor = "Branco"
        elif escC == 3:
            self.__cor = "Amarelo"
        else:
            print("Valor inválido")

    def dimensoes(self):
        escD = int(input("\nSelecione a largura: \n[1] - 60 \n[2] - 70 \n[3] - 80 \n[4] - 90 \n[ ] - Escolha: "))
        if escD == 1:
            self.__largura = 60
        elif escD == 2:
            self.__largura = 70
        elif escD == 3:
            self.__largura = 80
        elif escD == 4:
            self.__largura = 90
        else: 
            print("Valor inválido")
        
    def tipo_largura(self):
        if self.__largura == None:
            return "Largura indefinida"
        else:
            return self.__largura

    def abrir_porta(self):
        self.__aberta = True
        time.sleep(0.5)
        print("| Porta aberta")
        
    def fechar_porta(self):
        self.__aberta = False
        time.sleep(0.5)
        print("| Porta fechada")

    def __tipo_pintura(self):
        if self.__cor == None:
            return "Sem cor"
        return self.__cor

    def __aberta_fechada(self):
        estado = self.__aberta
        if estado:
            return "Aberta"
        return "Fechada"

    def __str__(self):
        return f"\n| PORTA | \nCor: {self.__tipo_pintura()} | Estado: {self.__aberta_fechada()} | Altura: {self.__altura} | Largura: {self.tipo_largura()}"


def menu():

    porta = Porta()
    while True: 
        time.sleep(0.5)
        menu = int(input("""
|-------MENU-------|        
[1] - Escolher cores
[2] - Escolher largura
[3] - Abrir porta
[4] - Fechar porta
[5] - Descrição da porta
[6] - Sair
[ ] - Escolha: """))

        if menu == 1:
            porta.cores()
        elif menu == 2:
            porta.dimensoes()
        elif menu == 3:
            porta.abrir_porta()
        elif menu == 4:
            porta.fechar_porta()
        elif menu == 5:
            print(porta)
        elif menu == 6:
            break
        else:
            print("| Valor inválido")

menu()