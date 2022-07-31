Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-11
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Dados em Python - Tuplas
Olá pessoal!


Vamos dar prosseguimento aos posts falando sobre Estruturas de Dados em Python.

Já falamos sobre Listas em Python e Dicionários em Python.

Hoje, o tema são as tuplas. Tuplas são estruturas de dados ordenadas e que não permitem alteração após sua criação. Elas são usadas em muitas situações no Python.

Vejamos então formas de criar tuplas:

t = () # uma tupla vazia
t1 = 1, 2, 3, 4 # uma tupla com valores
t2 = (1, 2, 3, 4) # igual a t1, mas criada usando parênteses
t3 = ('abracadabra', ) # tuplas de 1 elemento sempre são 
                       # criadas com parênteses e uma virgula
t4 = ('casa',3, 4.12, t2, t1) # tupla contendo objetos diferentes 

Algo importante a se observar é que diferentemente das listas, as tuplas não podem ser alteradas, não havendo então métodos de remoção, inserção ou alteração de elementos. Isto faz com que este seja um tipo de dados imprescindível para a passagem de parâmetros para funções como veremos mais à frente ao falarmo das funções.

Uma das principais formas de utilizar as tuplas (e muitas vezes fazemos sem saber que estamos fazendo) é empacotamento de dados.

Por exemplo, se temos as coordenadas de um ponto:

>>> x = 1.0
>>> y = 3.0

Podemos empacotar as coordenadas em uma tupla

>>> ponto = x, y

Se em um determinado momento precisarmos recuperar estes valores, basta fazermos o inverso, desempacotando os dados.

>>> x, y = ponto

Um detalhe que deve ser comentado aqui é que empacotar dados sepre gera uma tupla, mas o inverso pode ser feito com qualquer sequência.

Bem... vamos deixar as utilizações mais poderosas a seu tempo... Tudo a seu tempo.

Espero que tenham compreendido o que é e como funciona uma tupla.

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!

Até a próxima!
