## Exercícios de lógica de programação usando Python

### ENUNCIADOS (clique nas setas para expandir)

<details><summary>Exercício 1</summary>
<h3>Faça um algoritmo que implemente o menu abaixo.</h3>

MENU<br/>
1- Cadastrar Login e Senha<br/>
2- Aumento de 10%<br/>
3- Relatório<br/>
4- Cadastrar Funcionário<br/>
Escolha:

Para implementar seu código você deverá utilizar
as seguintes listas:<br/>
login = []<br/>
senha = []<br/>
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']<br/>
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]

<h3>Descrição:</h3> <br/>
Na opção 1 - Você deverá cadastrar login e senha nas listas correspondentes.
             Critério: login não poderá se repetir. Verificar se nome consta
             na lista de funcionarios.
<br/>
<br/>
Para executar as opções 2 e 3, você deverá validar seu login e senha.
<br/>
<br/>
Na opção 2 - Após validar login e senha, seu código deverá aumentar
             o salário dos funcionários em 10%. Mas somente
             se o funcionário ganhar abaixo da média em relação
             a lista de salarios.
<br/>
<br/>
Na opção 3 - Após confirmar login e senha, você deverá fazer um
             relatório mostrando o nome e o salario, conforme exemplo:

                 Maria Clara  - 7450.23
                 João Antonio - 5677.33
                 Carlos       - 3970.34
                 Pedro        - 3470.00
                 Ana          - 2200.00

Na opção 4 - Você deverá cadastrar o nome e o salário de um
             novo funcionário.

</details>
<details><summary>Exercício 2</summary>
<h3>Faça um algoritmo que resolva o problema abaixo.</h3>

Um vendedor necessita de um algoritmo que calcule o preço total devido por<br/>
um cliente em compras. O algoritmo deve ler o nome do cliente, o código de um<br/>
produto e a quantidade comprada de cada item. Calcular o preço total por item.<br/>
<br/>
Quando o código digitado for 'fim' deve encerrar o programa e<br/>
mostrar o total a ser pago de todos itens digitados.


        TABELA DE PRODUTOS E PREÇOS
      Código do Produto - Preço unitário
            1001     -    5.32
            1324     -    6.45
            6548     -    2.37
            2987     -    5.32
            7623     -    6.45

EXEMPLO: Ao ser digitado 'fim' mostrar o resumo das compras:

        Nome: Pedro
        Produto - Qtd.  -      Preço
        1001  -    2    -      10.64
        2987  -    1    -       5.32
        6548  -    3    -       7.11
        Total:     -    -      23.07


lista_produtos = ['1001', '1324', '6548', '2987', '7623']<br/>
lista_preços =   [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ]

</details>

<details><summary>Exercício 3</summary>
<h3>Crie uma classe chamada Caneta com os seguintes atributos:</h3>
        - marca</br>
        - cor</br>
        - tipo_ponta</br>
        - tampada</br></br>
    O atributo marca deve ser do tipo string.</br>
        > Exemplos: "BIC", "FABER CASTEL", "UNI BALL"</br>
    O atributo cor deve ser do tipo string.</br>
        > Exemplos: "Azul", "Preta", "Vermelha"</br>
    O atributo tipo_ponta deve ser um valor real.</br>
        > Exemplos: 0.7, 0.5, 0.3)</br>
    O atributo tampada dever um boleano. (True, False)</br>
        > O padrão de instância é True</br></br>

    Crie os métodos para:
        - escrever
        - tampar
        - destampar
        - dados_caneta
            -> Este método deverá retornar uma string com os atributos
                do objeto

    Crie uma lista para armazenar as suas canetas.
    Crie as seguintes funções:
        - adicionar_canetas_na_lista
        - listar_todas_canetas
        - escolher_caneta.
            -> Esta função deverá retornar uma caneta escolhida da lista.
        - colocar_caneta_lixo   (retirar da lista)

</details>

<details><summary>Exercício 4</summary>

<h3>Crie uma classe chamada 'Lampada', com um atributo:</h3>
            > 'estado' - Este atributo deverá ser um valor boleano</br>
            > 'True', quando a lampada estiver acessa e</br>
            > 'False', quando a lampada estiver apagada.</br>
    <h4>A classe 'Lampada' deverá ter no contrutor o estado sempre em FALSE.</h4>

    Crie os métodos necessários para ligar e desligar a lâmpada.
    Crie também um método que retorne uma string "LIGADA", ou "DESLIGADA"
        conforme o estado. (LIGADA - True,  DESLIGADA - False)

    Você deverá controlar as ações da lâmpada pelo menu abaixo:
        MENU
        1- Ligar a lâmpada
        2- Desligar a lâmpada

    Para cada iteração realizada na lâmpada você deverá imprimir
    seu estado.

    Exemplo:
        lampada = 'LIGADA'
        lampada = 'DESLIGADA'

> Obs.:  
    Você consegue alterar o código a cima para mais que uma lâmpada?
    Como ficaria? Tente!

</details>

<details><summary>Exercício 5</summary>

<h3>Crie uma classe Porta, com os atributos:</h3>
   	
   	> cor: (None: significa não pintada) ou
      	     "VERMELHA", "BRANCA", "AMARELA"
    > altura: (210: altura padrão em centímetros)
   	> largura: (60, ou 70, ou 80, ou 90 cm )
   	> aberta: (False: se porta fechada - True: se porta aberta).
   	observação: Todos atributos devem ser privados


	 Faça os métodos:
   	- construtor, passando a largura desejada
                   e altura como default em 210.
   	- pintar (parâmetro é uma nova cor)
   	- abrir_porta
   	- fechar_porta
   	- __str__: (mostrar todos atributos)

	   - crie um método privado 'tipo_pintura' que retorne
     	  "SEM COR", caso a porta não esteja pintada
      	 	ou retorne a cor atual
   	- crie um método privado 'aberta_fechada' que retorne
       		"ABERTA" ou "FECHADA", conforme True ou False
   	- altere o __str__ para chamar esses métodos.

</details>

<details><summary>Exercício 6</summary>

<h3>Faça um algoritmo que controle o acesso de pessoas a
um estabelecimento comercial.</h3>

	Para isso você deverá utilizar as seguintes classes:

	Crie uma classe Profissional com os atributos:
		- nome
		- especialidade
		- sala
	    Todos atributos devem ser privados e string.

	crie uma classe Visitante com os atributos:
		- nome
		- documento
	    Todos atributos devem ser privados e string.

	crie a classe Visita com os atributos:
		- visitante
		- profissional
		- data_visita
	    O atributo visitante deverá ser um objeto da
		classe Visitante escolhido de lista_visitantes.
	    O atributo profissional deverá ser um objeto da
		classe Profissional escolhido de lista_profissionais.

	Crie os métodos que forem necessários para acessar os
	atributos das classes.


	Desenvolva seu código a partir do menu abaixo:

	======================
	MENU
	======================
	1- Cadastrar Profissional
	2- Localizar Profissional
	3- Cadastrar Visitante
	4- Registrar Visita
	5- Relatório de Conferência
	Escolha:


	Na opção 1 do menu cadastre o nome, especialidade e sala
	    onde o profissional atende. Armazene esses dados em
	    lista_Profissionais (como objetos).

	Na opção 2 do menu é possível localizar um profissional
	    pelo nome ou pela profissão. Isso serve para o caso
	    do visitante não saber a sala do profissional.
	    (Apenas mostrar na tela o nome e a sala do profissional)

	Na opção 3 do menu será cadastrado o visitante com nome,
	    documento. Armazene esses dados em lista_visitantes
	    (como objetos).

	Na opção 4 do menu será registrado a visita.
	    Escolha o visitante (da lista de visitantes) e o
	    profissional (da lista_profissionais), entre com a
	    data e armazene a visita em lista_visitas
	    (como objeto).

	Na opção 5 do menu apenas crie um relatório de conferência.
	    Selecione o Profissional e mostre todos os visitantes
	    e a data da visita.

	Obs. Em todas as listas serão armazenados as instâncias
	de suas classes.



</details>
