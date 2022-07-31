Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-9
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Dados em Python - Listas: List Comprehention
Boa noite pessoal!

Como prometido, hoje vamos continuar o post de ontem, falando sobre listas em Python, pois este é uma assunto bastante extenso.


O assunto de hoje é List Comprehension, ou em português, abrangência de listas. Como o termo em português não retrata bem o que este recurso faz, vamos usar o termo em inglês mesmo.


List Comprehension é um recurso do Python que permite a criação de listas de forma simples, usando simplesmente uma expressão seguida de um for que pode conter outros for e/ou if dentro dele.

Tudo ficará mais claro ao partirmos para os exemplos.

Então, vamos colocar a mão na massa! Abra o shell do Python.

Lembre-seque o que deve ser digitado estará precedido de >>> ou ..., assim como aparecerá no shell do python.

Se por acaso você não entendeu do que estou falando, é aconselhável que você leia antes os posts anteriores que te deixarão em dia com tudo que vimos até agora.

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

Agora chegamos ao ponto em que devemos responder o desafio de ontem para prosseguir.

No último post, ficou um desafio: "Quem imagina como fazer uma matriz em Python usando o que vimos hoje???"

A resposta é: Criar listas de listas!

Então, se fizermos:

>>> m = [[1, 2, 3],[2, 3, 4]]

Teremos a matriz m com 2 linhas e 3 colunas, contendo na primeira linha os valores 1, 2, 3 e na segunda os valores 2, 3 e 4.

Assim, podemo usar list comprehention também para criarmos matrizes. Chamamos este recurso de Nested List Comprehention (nested = aninhado).

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

Acho que por hoje, este recurso está bem ilustrado. Qualquer dúvida, postem nos comentários que a resposta será rápida!

Comentem!

Assinem o Feed e não percam nenhum Post do Programe em Python!

Abraços!
