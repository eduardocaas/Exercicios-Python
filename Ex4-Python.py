import time
import sys

class Lampada:

    def __init__(self, estado = False):

        self.estado = estado

    def ligar(self):
        self.estado = True
        print("\n| Lâmpada ligada!")
        
    def desligar(self):
        self.estado = False
        print("\n| Lâmpada desligada!")

    def queimar(self):
        a = 0
        print()
        while a <= 5:
            time.sleep(0.3)
            print("| Lâmpada ligada!")
            time.sleep(0.3)
            print("| Lâmpada desligada!")
            a += 1
        print("\n!!!!! LÂMPADA QUEIMADA !!!!!")
        self.estado = "LÂMPADA QUEIMADA"
        
    def nm(self):
        if self.estado == bool(True):
            return "\n| A lâmpada está ligada"
        elif self.estado == str("LÂMPADA QUEIMADA"):
            return "\n| A lâmpada está queimada"
        else:
            return "\n| A lâmpada está desligada"

    def status(self):
        print(self.nm())

lampadas = []


def menu(lamp):
    while True:
        menu = int(input("""
| 1 - Status da lâmpada
| 2 - Ligar
| 3 - Desligar 
| 4 - Queimar
| 5 - Sair
| Escolha: """))

        if menu == 1:
            lamp.status()
        elif menu == 2:
            if lamp.estado == str("LÂMPADA QUEIMADA"):
                print(lamp.nm())
            else:
                lamp.ligar()
        elif menu == 3:
            if lamp.estado == str("LÂMPADA QUEIMADA"):
                print(lamp.nm())
            else:
                lamp.desligar()
        elif menu == 4:
            if lamp.estado == str("LÂMPADA QUEIMADA"):
                print("\n| A lâmpada já está queimada!")
            else:
                lamp.queimar()
        elif menu == 5:
            print("\n| Saindo...")
            break

def adicionar_lampadas():
    for i in range(int(input("\n| Quantas lâmpadas: "))):
        lampadas.append(Lampada())


def mostrar():
    print()
    for x in range(len(lampadas)):
        print(f"| Lâmpada {x+1}: " + lampadas[x].nm() + "\n")


def escolha():
    mostrar()
    esc_lmp = int(input("| Escolha: "))
    menu(lampadas[esc_lmp-1])


while True:
    esc = int(input("""\n| 1 - Adicionar lâmpadas
| 2 - Consultar lâmpadas
| 3 - Ações nas lâmpada(s)
| 4 - Sair
| Escolha: """))

    if esc == 1: 
        adicionar_lampadas()
    elif esc == 2:
        mostrar()
    elif esc == 3:
        escolha()
    elif esc == 4: 
        break