Title: Python 101 - Parte 10 - Dicionários
Date: 2022-08-30 00:06
Slug: python-101-parte-10
Category: Tutoriais
Tags: Tutorial, Python 101

Olá!

Hoje vamos falar de uma estrutura de dados que não está presente em todas as linguagens. Esta estrutura é chamada de dicionário.

Os dicionários em Python são estruturas de dados que contém pares de chave-valor.

São parecidos com as listas, considerando que ambos são sequencias de elementos, mas o acesso a cada posição da lista é feito de forma diferente.

Caso você ainda não tenha visto os outros artigos da série Python 101, aqui estão:

* [Introdução ao Python]({filename}/Tutoriais/python101.md)
* [Blocos de Código em Python]({filename}/Tutoriais/python101.2.md)
* [Estruturas Condicionais em Python - 1]({filename}/Tutoriais/python101.3.md)
* [Estruturas Condicionais em Python - 2]({filename}/Tutoriais/python101.4.md)
* [Estruturas de Repetição - while]({filename}/Tutoriais/python101.5.md)
* [Estruturas de Repetição - for]({filename}/Tutoriais/python101.6.md)
* [Estruturas de Dados do Python - 1]({filename}/Tutoriais/python101.7.md)
* [Estruturas de Dados do Python - Listas]({filename}/Tutoriais/python101.8.md)
* [Estruturas de Dados do Python - Lista Comprehentions]({filename}/Tutoriais/python101.9.md)

Vejamos então como trabalhar com Dicionários em Python!

Para começar, vamos ver as maneiras de definir um dicionário.

Primeiro definimos um dicionário vazio:

    #!python
    dicionario = {}

Este dicionário pode receber valores futuramente durante a execução do programa.

Agora, imaginemos como seria montar um dicionário que relacionasse strings para os dias da semana, como 'seg' e 'ter' com números. Indispensável se você for fazer um calendário, não acha?

    #!python
    dias_semana = {'dom' : 0, 'seg' : 1, 'ter' : 2, 'qua' : 3,
        'qui' : 4, 'sex' : 5, 'sab' : 6}

Ao criarmos um dicionário, ele terá esta estrutura. Antes do ':' temos a chave do par chave-valor, e logo após, o valor correspondente.

Mas, e se fôssemos criar um dicionário que relacionasse as letras N, L, S, O dos pontos cardeais com números?

Aposto que você já sabe a resposta! Mas, existe uma outra forma, também muito útil de gerar dicionários, e que pode ser muito importante para geração destes dicionários em tempo de execução.

Usando `dict()` podemos transformar listas de tuplas em dicionários. Tecnicamente seriam sequencias de sequencias, mas para o exemplo vamos usar listas de tuplas.

> Se você não lembra o que é uma tupla, confira nosso [post de introdução às estruturas de dados]({filename}/Tutoriais/python101.7.md)

Veja como funciona o `dict()`:

    #!python
    pontos_cardeais = dict([('N', 0), ('L', 1), ('S', 2), ('O', 3)])

Você se lembra da [List Comprehension]({filename}/Tutoriais/python101.9.md) que vimos no último post?

Pois bem, que tal usá-la para montar um dicionário que relaciona os inteiros de zero a dez e seus respectivos quadrados?

    #!python
    quadrados = dict([x, x**2 for x in range(11)])

É muito simples criar dicionário, não?

Mas... simplesmente criar os dicionários não tem utilidade nenhuma, certo?

Vejamos como acessar um valor a partir de sua chave. vamos usar o dicionário dos dias da semana. Experimente os comandos no Shell do Python!

    >>> dias_semana['ter']
    2
    >>> dias_semana['sab']
    6

Fácil, não é?

Vamos inserir alguns valores neste dicionário?

    >>> dias_semana
    {'qua': 3, 'dom': 0, 'sab': 6, 'sex': 5, 'seg': 1, 'qui': 4, 'ter': 2}
    >>> dias_semana['Dom'] = 0
    >>> dias_semana['Seg'] = 1
    >>> dias_semana['Ter'] = 2
    >>> dias_semana['Qua'] = 3
    >>> dias_semana['Qui'] = 4
    >>> dias_semana['Sex'] = 5
    >>> dias_semana['Sab'] = 6
    >>> dias_semana
    {'qua': 3, 'dom': 0, 'sab': 6, 'Dom': 0, 'Seg': 1, 'sex': 5, 'seg': 1, 
    'Qui': 4, 'Qua': 3, 'Sab': 6, 'qui': 4, 'ter': 2, 'Sex': 5, 'Ter': 2}

Num dicionário, a ordem em que os elementos aparecem não é tão importante, pois os valores são acessados principalmente através de suas respectivas chaves, e não de suas posições. Além disso, dicionários não guardam a ordem dos elementos, logo, o elemento que aparece em primeiro lugar numa execução pode não ser o primeiro em outra mesmo que a inserção tenha sido feita da mesma forma.

Caso seja necessário verificar se uma chave já se encontra no dicionário, basta fazer o seguinte

    >>> 'seg' in dias_semana
    True
    >>> 'bla' in dias_semana
    False

Bem, digamos agora que não quero mais que o dicionário tenha a versão maiúscula para o domingo.

    >>> del(dias_semana['Dom])

Também é possível saber quais as chaves que já foram inseridas:

    >>> dias_semana.keys()
    ['sab', 'seg', 'sex', 'qua', 'qui', 'ter', 'Qua', 'dom', 'Sab', 'Sex',
    'Seg', 'Qui', 'Ter']

E quais os valores que há no dicionário:
    >>> dias_semana.values()
    [6, 1, 5, 3, 4, 2, 3, 0, 6, 5, 1, 4, 2]

Algo importante a se notar é que as chaves e elementos de dicionários podem ser de virtualmente qualquer tipo, com exceção das chaves que tem uma restrição. Os objetos tem que ser imutáveis.

Isto quer dizer que a lista `[1, 2, 3]` não pode ser uma chave de dicionário já que podemos no meio da execução alterar valores da lista. Já a tupla `(1, 2, 3)` que é imutável pode ser uma chave de dicionários sem problemas.

Agora, você já conhece os Dicionários do Python, esta estrutura de dados que tem tantas aplicações importantes.

Não deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!