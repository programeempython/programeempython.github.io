Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-2
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Agora que já temos o Python instalado e já conhecemos a sua interface interativa, vamos aprender um pouco sobre os comandos mais básicos da linguagem!

Antes de continuarmos, se não leu o post anterior, acesse aqui:

[Python 101 - Primeira Parte]({filename}/Tutoriais/python101.md)

Como visto, no shell Python, temos dois cursores:

    >>>
    ...

Ao fazermos um if, estrutura condicional que será explicada em mais detalhes num próximo post, temos o seguinte no console:

    >>> x = 0
    >>> if x < 1:
    ...     print("x é menor que 1")
    ... 
    x é menor que 1

Agora, a explicação =]

Na primeira linha, dizemos que a variável x contém o valor 0;
Em seguida, comparamos o valor contido em x com 1. Ao terminarmos um comando com : o interpretador entende que este é um comando que não acabou no final daquela linha, e que é composto por mais comandos, então surge o cursor secundário `...`.

Então, muitos programadores habituados com outras linguagens devem se perguntar onde estão as chaves pra determinar o bloco.

No Python, os blocos são determinados pela identação (ou edentação, ou endentação... já vi várias formas da palavra).

As linhas que estão dentro do if, ou seja o que deve ser executado caso a comparação seja verdadeira deve estar identado.

Em geral é uma convenção, no Python, usarmos 4 espaços para a identação.

O `print("x é menor que 1")` é o comando que deve ser executado se a comparação `x < 1` for verdadeira. Assim, esta linha está identada, e o interpretador sabe que só deve executá-la caso *x* seja menor que *1*.

Quando você dá um `ENTER` no final desta linha, o interpretador te mostra novamente o cursor secundário, pois um `if` pode ter vários comandos ali dentro. Como veremos mais adiante a execução de um programa todo pode estar dentro de um __if__.

Assim, só depois de um segundo `ENTER` é que o interpretador executa o comando e mostra o resultado.

Então, recapitulando:

* Blocos em Python são definidos pela identação
* A identação deve seguir um padrão, preferencialmente em todos os programas
* É convenção usar 4 espaços para identação
* No interpretador, blocos identados são precedidos do cursos secundário ...
* Um bloco indica um trecho de código que está dentro de outro comando

Por enquanto é só!

No próximo post aproveitamos a deixa, e falamos sobre estruturas condicionais em Python!

Não deixe de deixar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!