Title: Python 101 - Parte 3 - Estruturas Condicionais em Python
Date: 2022-08-01 23:06
Modified: 2022-08-07 13:25
Slug: python-101-parte-3-condicionais
Category: Tutoriais
Tags: Tutorial, Python 101, Condicionais

Olá!

Continuando nossa série introdutória sobre Python, vamos falar um pouco sobre as estruturas condicionais.

Caso não tenha visto os tutoriais anteriores, já temos:

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)

As estruturas condicionais são essenciais na programação. Sem elas, os programas seriam chatos, monótonos, e nunca teriam a capacidade toda que temos atualmente.

__Sem estruturas condicionais não haveria jogos eletrônicos!!!!__

Então, vejamos como o Python implementa suas estruturas condicionais.

A principal estrutura condicional do Python (e mais usada também) é a construção `if`/`else` ou sua variação `if`/`elif`/`else`.

`if`, traduzindo do inglês quer dizer se, e else senão, logo, estas construções nos permitem orientar a execução de um trecho de código. Se isso, faz aquilo, senão, faz aquilo outro...

Veja abaixo um exemplo de utilização do if/else:

    #!python
    x = 3
    if x % 2 == 0:
        print("x é par")
    else:
        print("x é impar")

Este código analisa o valor da variável `x`. Se `x % 2` (o resto da divisão de `x` por `2`) for igual a zero, então o número é par, senão, é impar. Veremos mais funções matemáticas em posts futuros.

Ao digitar estes comando no terminal, ficaria assim:

    >>> x = 3
    >>> if x % 2 == 0:
    ...     print("x é par")
    ... else:
    ...     print("x é impar") 
    ...
    x e impar 

Recapitulando o que foi dito no texto sobre blocos de código em Python, quando temos um bloco identado logo abaixo de um comando terminado em :, temos um bloco que está diretamente relacionado a este comando.

No exemplo, temos o comando `if x%2==0:` e logo abaixo o print `"x é par"` identado. Isto quer dizer que o código identado (`print("x é par")`) somente será executado se o resto da divisão de `x` por `2` for zero.

Caso este resultado seja diferente de zero, x não é par, e o interpretador encontra o comando `else:`.

Logo abaxo deste comando, temos `print("x é impar")` que está identado, mostrando ao interpretador que este é o comando que deve ser executado caso a comparação dentro do `if` seja falsa.

Não vamos esticar o assunto. Por enquanto paramos por aqui, mas espere que logo teremos a continuação pra você!

Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!