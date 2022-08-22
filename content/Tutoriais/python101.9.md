Title: Python 101 - Parte 9 - Estruturas de Dados - List Comprehention
Date: 2022-08-22 23:06
Slug: python-101-parte-9
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Como prometido, hoje vamos continuar o post falando sobre listas em Python, pois este é uma assunto bastante extenso.

O assunto de hoje é __List Comprehension__, ou em português, abrangência de listas. Como o termo em português não retrata bem o que este recurso faz, vamos usar o termo em inglês mesmo.

__List Comprehension__ é um recurso do Python que permite a criação de listas de forma simples, usando simplesmente uma expressão seguida de um `for` que pode conter outros `for` e/ou `if` dentro dele.

Tudo ficará mais claro ao partirmos para os exemplos.

Então, vamos colocar a mão na massa! Abra o shell do Python.

Lembre-se que o que deve ser digitado estará precedido de `>>>` ou `...`, assim como aparecerá no shell do python.

Se por acaso você não entendeu do que estou falando, é aconselhável que você leia antes os posts anteriores que te deixarão em dia com tudo que vimos até agora.

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)
* [Estruturas Condicionais em Python - 1]({filename}/Tutoriais/python101.3.md)
* [Estruturas Condicionais em Python - 2]({filename}/Tutoriais/python101.4.md)
* [Estruturas de Repetição - while]({filename}/Tutoriais/python101.5.md)
* [Estruturas de Repetição - for]({filename}/Tutoriais/python101.6.md)
* [Estruturas de Dados do Python - 1]({filename}/Tutoriais/python101.7.md)
* [Estruturas de Dados do Python - Listas]({filename}/Tutoriais/python101.8.md)

Procure entender exatamente o que acontece em cada exemplo. Vamos lá!

    >>> l = [1, 2, 4] 
    >>> [3 * x for x in l]
    [3, 6, 12]
    >>> [2 * x for x in l if x > 3]
    [12]
    >>> 5 * x for x in l if x < 0] 
    []
    >>> [[x, 2*x] for x in l]
    [[1, 2], [2, 4], [4, 8]]
    >>> [(x, 2*x) for x in l]
    [(1, 2), (2, 4), (4, 8)]
    >>> l1 = [0, 1, 2]
    >>> l2 = [1, 2, 3]
    >>> [x * y for x in l1 for y in l2] 
    [0, 0, 0, 1, 2, 3, 2, 4, 6]
    >>> [l1[i] * l2[i] for i in range(len(l1))]
    [0, 2, 6]

As instruções são sempre dadas no mesmo padrão:

    [<expressao> for <variável> in <lista> [if <condição>] [for...]]
    *** As estruturas entre [] são opcionais. ***

Agora chegamos ao ponto em que devemos responder ao desafio do último post da série Python 101 para prosseguir.

> "Quem imagina como fazer uma matriz em Python usando o que vimos hoje?"

A resposta é: **Criar listas de listas!**

Então, se fizermos:

    >>> m = [[1, 2, 3],[2, 3, 4]]

Teremos a matriz m com 2 linhas e 3 colunas, contendo na primeira linha os valores `1, 2, 3` e na segunda os valores `2, 3, 4`.

Assim, podemo usar `list comprehention` também para criarmos matrizes. Chamamos este recurso de Nested List Comprehention _(nested = aninhado)_.

Vejamos o seguinte exemplo:

    >>> m = [
    ...         [1, 2, 3],
    ...         [4, 5, 6],
    ...         [7, 8, 9],
    ...     ]

Aqui, criamos uma matriz 3x3 com os valores de 1 a 9.
Agora, veja uma forma de trocar as linhas com as colunas da matriz m:

    >>> [[linha[i] for linha in m] for i in [0, 1, 2]]
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Acho que por hoje, este recurso está bem ilustrado. Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!
