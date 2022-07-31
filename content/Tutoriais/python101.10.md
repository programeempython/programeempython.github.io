Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-10
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Dados em Python - Dicionários
Boa Noite Pessoal!

Hoje vamos falar de uma estrutura de dados que não está presente em todas as linguagens. Esta estrutura é chamada de dicionário.

Os dicionários em Python são estruturas de dados que contém pares de chave-valor.


São parecidos com as listas, mas o acesso a cada posição da lista é feito de forma diferente.

Vejamos então como trabalhar com Dicionários em Python!

Para começar, vamos ver as maneiras de definir um dicionário.

Primeiro definimos um dicionário vazio:
dicionario = {}
Este dicionário pode receber valores futuramente durante a execução do programa.

Agora, imaginemos como seira montar um dicionário que relacionasse strings para os dias da semana, como 'seg' e 'ter' com números. Indispensável se você for fazer um calendário, não acha?
dias_semana = {'dom' : 0, 'seg' : 1, 'ter' : 2, 'qua' : 3,\
              'qui' : 4, 'sex' : 5, 'sab' : 6}
Ao criarmos um dicionário, ele terá esta estrutura. Antes do ':' temos a chave do par chave-valor, e logo após, o valor correspondente.

Mas, e se fôssemos criar um dicionário que relacionasse as letras N, L, S, O dos pontos cardeais com números?

Aposto que você já sabe a resposta! Mas, existe uma outra forma, também muito útil de gerar dicionários, e que pode ser muito importante para geração destes dicionários em tempo de execução.

Este método (dict()) permite transformar listas de tuplas em dicionários.
*** se você não lembra o que é uma tupla, confira aqui ***

Veja como funciona o método dict():
pontos_cardeais = dict([('N', 0), ('L', 1), ('S', 2), ('O', 3)])
Você se lembra da List Comprehension que vimos no último post?

Pois bem, que tal usá-la para montar um dicionário que relaciona os inteiros de zero a dez e seus respectivos quadrados?
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
Num dicionário, a ordem em que os elementos aparecem não é importante, pois os valores são acessados somente através de suas respectivas chaves, e não de suas posições.

Caso seja necessário verificar se uma chave já se encontra no dicionário, basta fazer o seguinte
>>> 'seg' in dias_semana
True
>>> 'bla' in dias_semana
False
Bem, digamos agora que não quero mais que o dicionário tenha a versão maiúscula para o domingo.
>>> del dias_semana['Dom]
Também é possível saber quais as chaves que já foram inseridas:
>>> dias_semana.keys()
['sab', 'seg', 'sex', 'qua', 'qui', 'ter', 'Qua', 'dom', 'Sab', 'Sex',
'Seg', 'Qui', 'Ter']
E quais os valores que há no dicionário:
>>> dias_semana.values()
[6, 1, 5, 3, 4, 2, 3, 0, 6, 5, 1, 4, 2]
Agora, você já conhece os Dicionários do Python, esta estrutura de dados que tem tantas aplicaçãoes importantes.

Veja a seguir o primeiro  post de nível mais avançado do Programe em Python e aprenda a fazer um switch com dicionários!

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!

Até a próxima!