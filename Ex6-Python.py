from datetime import datetime


lista_visitantes = []    # Listas de objetos
lista_profissionais = []
lista_visitas = []


class Profissional:

    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def getNome(self):  # Setters e Getters
        return self.__nome

    def getSala(self):
        return self.__sala

    def getEspecialidade(self):
        return self.__especialidade

    def __str__(self):
        return f"Profissional: {self.__nome}  Especialidade: {self.__especialidade}  Sala: {self.__sala}"


class Visitante:

    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def getNome(self):  # Setters e Getters
        return self.__nome

    def __str__(self):
        return f"Visitante: {self.__nome}  Documento: {self.__documento}"


class Visita:

    def __init__(self):
        self.__visitante = None
        self.__profissional = None
        self.__data = None

    def setVisitante(self, visitante):  # Setters e Getters
        self.__visitante = visitante

    def setProfissional(self, profissional):
        self.__profissional = profissional

    def setData(self, data):
        self.__data = data

    def __str__(self):
        return f"Profissional: {self.__profissional.getNome()} --- Visitante: {self.__visitante.getNome()} --- Sala: {self.__profissional.getSala()} --- Data: {self.__data}"


def cadastrar_profissional():
    print("========CADASTRAR PROFISSIONAL========")
    nome = str(input("Digite o nome: "))
    espc = str(input("Digite a especialidade: "))
    sala = str(input("Digite a sala: "))

    profissional = Profissional(nome, espc, sala)
    lista_profissionais.append(profissional)  # Criando profissional e adicionando a lista de profissionais
    print("\nPROFISSIONAL REGISTRADO")


def cadastrar_visitante():
    print("========CADASTRAR VISITANTE========")
    nome = str(input("Digite o nome: "))
    docm = str(input("Digite o documento: "))

    visitante = Visitante(nome, docm)
    lista_visitantes.append(visitante)  # Criando visitante e adicionando a lista de visitantes
    print("\nVISITANTE REGISTRADO")


def localizar_profissional():
    dados = str(input("Digite o nome ou especialidade do profissional: "))
    print("========LOCALIZADOS========")
    for x in range(len(lista_profissionais)):  # Localizando profissional e consultando a lista de profissionais
        if dados == lista_profissionais[x].getNome() or dados == lista_profissionais[x].getEspecialidade():
            print("= NOME: " + lista_profissionais[x].getNome() + "   SALA: " + lista_profissionais[x].getSala())


def registrar_visita():

    print("========REGISTRAR VISITA========")

    visita = Visita()

    for x, y in enumerate(lista_visitantes):
        print(x+1 , " - " , y)

    vist = int(input("Escolha o visitante: "))
    visita.setVisitante(lista_visitantes[vist-1])  # Adicionando visitante ao objeto visita

    print()

    for x, y in enumerate(lista_profissionais):
        print(x+1, " - ", y)

    prof = int(input("Escolha o profissional: "))
    visita.setProfissional(lista_profissionais[prof-1])  # Adicionando profissional ao objeto visita

    horario = datetime.now()
    horarioString = horario.strftime("%d/%m/%Y %H:%M:%S")

    visita.setData(horarioString)  # Adicionando horário ao objeto visita

    lista_visitas.append(visita)  # Adicionando visita a lista de visitas
    print("\nVISITA REGISTRADA")


def relatorio():
    print("========RELATÓRIO========")
    for x, y in enumerate(lista_visitas):  # Mostrando todas visitas registradas -> usando __str__ (Visita)
        print(lista_visitas[x])


p1 = Profissional("João", "Médico", "201")  # Criação de objetos (Profissional) para serem utilizados em teste de código
p2 = Profissional("Pedro", "Advogado", "304")
lista_profissionais.append(p1)
lista_profissionais.append(p2)

v1 = Visitante("José" , "2233")  # Criação de objetos (Visitante) para serem utilizados em teste de código
v2 = Visitante("Maria" , "21143")
v3 = Visitante("Carlos", "78912")
lista_visitantes.append(v1)
lista_visitantes.append(v2)
lista_visitantes.append(v3)


while True:
    menu = input("""\n========MENU========
[1] - Cadastrar Profissional
[2] - Localizar Profissional
[3] - Cadastrar Visitante
[4] - Registrar Visita
[5] - Relatório de Conferência
[6] - Sair
Escolha: """)
    if menu == '1':
        print()
        cadastrar_profissional()
    elif menu == '2':
        print()
        localizar_profissional()
    elif menu == '3':
        print()
        cadastrar_visitante()
    elif menu == '4':
        print()
        registrar_visita()
    elif menu == '5':
        print()
        relatorio()
    elif menu == '6':
        break
    else:
        print("\nOpção inválida")