Title: Python 101 - Parte 8 - Estruturas de Dados - Listas
Date: 2022-08-13 02:06
Slug: python-101-parte-8
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Vou falar hoje sobre Listas em Python.

Caso não tenha visto os tutoriais anteriores, já temos:

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)
* [Estruturas Condicionais em Python - 1]({filename}/Tutoriais/python101.3.md)
* [Estruturas Condicionais em Python - 2]({filename}/Tutoriais/python101.4.md)
* [Estruturas de Repetição - while]({filename}/Tutoriais/python101.5.md)
* [Estruturas de Repetição - for]({filename}/Tutoriais/python101.6.md)
* [Estruturas de Dados do Python - 1]({filename}/Tutoriais/python101.7.md)

Listas são conjuntos ordenados de dados. Em python, estes conjuntos podem conter vários tipos de dados misturados, visto que tudo em Python é objeto.

Assim, além de tipos de dados básicos como inteiros, números reais e texto, as listas podem conter qualquer outro objeto da linguagem.

Vejamos como as listas são criadas em python:

    #!python
    # Criando uma lista vazia
    l = []

    #Criando uma lista já com valores
    l1 = [1, 2, 3, 'a', 'd', l]

    #Criando uma lista de letras a partir de uma string
    l2 = list("abracadabra")

No primeiro comando, criamos uma lista vazia, que poderá ser preenchida futuramente. Em seguida, criamos uma lista, já atribuindo valores no momento da criação.

Perceba que ao criar a lista são passados valores inteiros, letras e a lista que foi criada vazia anteriormente. Assim, demonstramos que uma lista pode receber qualquer tipo de objeto, e que pode ter objetos de tipos diferentes ao mesmo tempo!

Na lista três, utilizamos `list()` para criar um objeto `list` a partir de um `string`. Isto é possível porque tanto listas quanto strings são sequências.

Mas, as listas em Python não são estáticas. Podemos inserir e retirar valores conforme bem quisermos a qualquer hora durante a execução do programa. Vejamos:

    #!python
    # vamos acrescentar valores à lista l criada anteriormente
    # append(o) insere um objeto o no final da lista
    l.append(1) # a lista ficará assim [1]
    l.append(3) # a lista ficará assim [1, 3] 
    
    # insert(i, o), insere o objeto o na posição i (a primeira posição é zero)
    l.insert(1, 2) # a lista ficará assim [1, 2, 3]
    l.insert(0, 5) # a lista ficará assim [5, 1, 2, 3]
    
    # remove(o) remove a primeira ocorrência do objeto o
    l.append(5) # a lista ficará assim [5, 1, 2, 3, 5]
    l.remove(5) # a lista ficará assim [1, 2, 3, 5]
    
    # pop(i) remove e retorna o objeto da posição i
    # pop() remove e retorna o último elemento da lista
    l.insert(3, 6) # a lista ficará assim [1, 2, 3, 6, 5]
    l.pop(3) # a lista ficará assim [1, 2, 3, 5] e retornará 6
    l.pop() # a lista ficará assim [1, 2, 3] e retornará 5
    
    #index(o) retorna o índice do objeto o
    l.index(3) # retorna 2
    l.append(3) # a lista ficará assim [1, 2, 3, 3]
    l.index(3) # continua retornando 2 pois é a primeira ocorrência do 3
    
    # count(o) conta quantas vezes o objeto o aparece na lista
    l.count(1) # retorna 1
    l.count(3) # retorna 2
    l.pop() # a lista ficará assim [1, 2, 3] e retorna 3
    
    # extend(L) estende a lista com a lista L
    l.extend([0, -1, -2]) # a lista ficará assim [1, 2, 3, 0, -1, -2]
    
    # sort() organiza os itens da lista nela mesma
    l.sort() # a lista ficará assim [-2, -1, 0, 1, 2, 3]
    
    # reverse() inverte os elementos da lista nela mesma
    l.reverse() # a lista ficará assim [3, 2, 1, 0, -1, -2]

Agora é hora de treinar!

Abram o terminal, e comecem a brincar com as listas! Vejam como funcionam os comandos!

> Uma dica! O comando `help` mostra informações sobre um comando! Experimente, após
> criar uma lista l, o comando:
>
>    \>\>\> help(l.sort)

No próximo post vamos falar de uma operação que tem tudo a ver com listas: List Comprehension.

> Um desafio!
> 
> Quem imagina como fazer uma matriz em Python usando o que vimos hoje?
> 
> Deixe sua resposta nos comentários!

Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!