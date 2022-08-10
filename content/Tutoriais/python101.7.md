Title: Python 101 - Parte 7 - Estruturas de Dados - 1
Date: 2022-08-11 00:29
Slug: python-101-parte-7
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Hoje vamos ver uma coisa muito importante no Python: as estruturas de dados nativas.

Caso não tenha visto os tutoriais anteriores, já temos:

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)
* [Estruturas Condicionais em Python - 1]({filename}/Tutoriais/python101.3.md)
* [Estruturas Condicionais em Python - 2]({filename}/Tutoriais/python101.4.md)
* [Estruturas de Repetição - while]({filename}/Tutoriais/python101.5.md)
* [Estruturas de Repetição - for]({filename}/Tutoriais/python101.6.md)

São vários os tipos de dados nativos do Python. Entre eles, os mais importantes, pois são essenciais para qualquer programa, são os tipos:

* `int` - números inteiro
* `float` - ponto flutuante, representando os números reais, basicamente
* `string` - cadeia de caracteres, ou basicamente, texto

Porém, em Python, diferente de outras linguagens, estes tipos de dados, assim como todas as outras estruturas da linguagem são objetos, desta forma, o tipo básico de tudo em python é `object`. Há muito a se discutir sobre tipos de dados, mas para simplificar consideraremos assim.

Voltando às estruturas de dados nativas, veremos que estas são conjuntos estruturados de objetos que podem conter elementos de qualquer outro tipo.

A primeira e talvez mais largamente usada destas estruturas é a `list`. Uma `list` implementa uma lista que pode conter virtualmente qualquer objeto, sendo composta por quantos tipos de objeto for necessário (diferente de algumas linguagens).

Desta forma, listas se tornam uma ferramenta muito poderosa dentro do Python. Teremos mais adiante um post focado especialmente nas listas e seus métodos.

Para criar uma lista, basta atribuir valores a ela da seguinte forma:

    #!python
    l = [1,2,3,4,5]

Assim como fizemos quando vimos como funciona o `for`.

Outra estrutura de dados muito importante e largamente usada é a `tuple` (tupla). Tuplas contém conjuntos de valores assim como as listas, porém se diferenciam destas principalmente pelo fato de as tuplas não poderem ser alteradas após sua criação, e as listas sim.

Vamos criar uma tupla:

    #!python
    t = (1,2,3,4,5)

Vejamos agora uma das estruturas de dados mais poderosas do Python, e que possui muitas possibilidades de utilização. Esta estrutura é o `dict` (dicionário) que relaciona pares de chave e valor.

Assim criamos um dicionário:

    #!python
    d = {'a':1, 'b':2,'c':3, 'd':4, 'e':5}

Finalmente, a última estrutura de dados nativa do Python que veremos hoje é o set (conjunto). Os sets representam conjuntos matemáticos. Assim, são sequências e uma característica interessante é que não possuem elementos repetidos.

Por exemplo, ao criar este set:

    #!python
    s = set([1, 1, 2, 3, 5, 7, 13, 17])

O conjunto será `[1, 2, 3, 5, 7, 13, 17]`, pois `1` aparecia 2 vezes na lista original, e no set ele aparece somente uma vez.

Nos Próximos posts, vamos ver em mais detalhes estas estruturas de dados :D

Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!