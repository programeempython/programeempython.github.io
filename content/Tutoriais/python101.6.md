Title: Python 101 - Parte 6 - Estruturas de Repetição - For
Date: 2022-08-09 12:06
Slug: python-101-parte-6
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Mais um post aqui ensinando Python para vocês e hoje veremos o `for`.

Caso não tenha visto os tutoriais anteriores, já temos:

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)
* [Estruturas Condicionais em Python - 1]({filename}/Tutoriais/python101.3.md)
* [Estruturas Condicionais em Python - 2]({filename}/Tutoriais/python101.4.md)
* [Estruturas de Repetição - while]({filename}/Tutoriais/python101.5.md)


Vamos começar com um exemplo simples:

    #!python
    l = [1, 2, 3, 4, 5]
    for i in l:
        print(i)

Aqui, inicialmente, começamos com algo que ainda não vimos: __listas__.

Começamos criando `l` como uma lista que contém uma sequência de números.

Então, esta lista é usada dentro do `for`.

_Em outras linguagens, determinamos o valor inicial da variável contadora, seu limite e o passo de iteração. Em python isso não acontece. Aqui, o for somente itera sobre sequências. Isto traz várias vantagens, como por exemplo, iterar sobre strings, ou listas de elementos variados._

_Será mostrado adiante porque este for não está em desvantagem frente ao for das outras linguagens._

Então, a cada iteração, a variável de iteração, neste caso `i`, recebe o elemento de uma posição da lista.

Assim, este trecho acima imprime na tela todos os valores contidos na lista `l`.

Vamos ver agora este trecho de código:

    #!python
    d = ['arroz', 'feijão', 'carne', 'batata']
    for i in d:
        print('Estou cozinhando ', i)

Este exemplo demonstra a utilização do `for` com listas que contém *strings*, mostrando que pode-se usar listas com qualquer objeto num `for`.

No `for` também podemos usar `break` e `continue`. Assim, podemos controlar ainda mais o comportamento do laço. Além disso, há uma característica no `for` do Python que o deixa muito poderoso: podemos usar um `else` ao final do `for` como no exemplo a seguir:

    #!python
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if i == 'h':
            break
        print(i)
    else:
        print('"h" não está na lista mas eu printo mesmo assim')


Usando o `else` no final, podemos controlar o que será executado ao final de um execução completa do `for` e o que será executado se o laço for quebrado por um `break`. Quando o laço é completamente percorrido sem uma quebra, a execução segue pra dentro do `else`!

Neste exemplo, a saída será algo assim:

    a
    b
    c
    d
    e
    f
    g
    "h" não está na lista mas eu printo mesmo assim

Isto é muito importante, pois evita que tenhamos que fazer testes complicados para detectar quando um `for` for quebrado por um `break` que será chamado em condições complexas.

Finalmente, muitos devem estar se perguntando: "Como este `for` pode ser tão poderoso se temos que definir as listas manualmente?"

O fato é que não temos que fazer manualmente se for uma lista de números (assim como não precisamos em outras linguagens).

Existe uma função em Python, range, que retorna uma _generator_ (objeto que pode ser iterado como uma lista, mas gera os valores durante a execução) de números no intervalo especificado. Veja o exemplo:

    #!python
    for i in range(50):
        if i%2 == 0:
            print(i, 'é par')
        else:
            print(i, 'é impar')

Quando fazemos range(50), teremos uma _generator_ que funcionará como uma lista de inteiros de 0 a 49. (experimente no shell).

Bem, pessoal! Por hoje é isso!

Agora falta pouco para iniciarmos uma programação efetiva em Python!

Nos Próximos Posts, tipos de dados nativos do Python!

Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!