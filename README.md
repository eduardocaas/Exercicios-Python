# Exercícios em Python

### Exercícios de lógica de programação usando Python
## ENUNCIADOS
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
