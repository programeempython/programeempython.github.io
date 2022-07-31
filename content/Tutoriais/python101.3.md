Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-3
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas Condicionais em Python Parte 1
Olá Pessoal!

Hoje vou fazer um post mais feliz! Resultados na faculdade todos bons! Acabei de passar em mais uma matéria =]

Bem... conforme prometido, vamos falar um pouco sobre as estruturas condicionais que temos em Python.

As estruturas condicionais são essenciais na programação. Sem elas, os programas seriam chatos, monótonos, e nunca teriam a capacidade toda que temos atualmente.



SEM ESTRUTURAS CONDICIONAIS NÃO HAVERIA JOGOS ELETRÔNICOS!!!!



Então, vejamos como o Python implementa suas estruturas condicionais.

A principal estrutura condicional do Python (e mais usada também) é a construção if/else ou sua variação if/elif/else.

if, traduzindo do inglês quer dizer se, e else senão, logo, estas construções nos permitem orientar a execução de um trecho de código. Se isso, faz aquilo, senão, faz aquilo outro...

Veja abaixo um exemplo de utilização do if/else:


    x = 3
    if x % 2 == 0:
        print "x e par"
    else:
        print "x e impar"

Este código analisa o valor da variável x. Se x % 2 (o resto da divisão de x por 2) for igual a zero, então o número é par, senão, é impar. Veremos mais funções matemáticas em posts futuros.

Ao digitar estes comando no terminal, ficaria assim:

    >>> x = 3
    >>> if x%2==0:
    ...     print "x e par"
    ... else:
    ...     print "x e impar" 
    ...
    x e impar 

Recapitulando o que foi dito no texto sobre Blocos de Código em Python, qundo temos um bloco identado logo abaixo de um comando terminado em :, temos um bloco que está diretamente relacionado a este comando.

No exemplo, temos o comando if x%2==0: e logo abaixo o print "x e par" identado. Isto quer dizer que o código identado (print "x e par") somente será executado se o resto da divisão de x por 2 for zero.

Caso este resultado seja diferente de zero, x não é par, e o interpretador encontra o comando else:.

Logo abaxo deste comando, temos print "x e impar" que está identado, mostrando ao interpretador que este é o comando que deve ser executado caso a comparação dentro do if seja falsa.

Não vamos esticar o assunto. Por enquanto paramos por aqui, mas espere que jajá tem a continuação pra você!

Comente!
Assine o Feed e não perca nenhum posto do Programe em Python!

Abraços!
Até a próxima!