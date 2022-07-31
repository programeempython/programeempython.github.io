Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-6
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Repetição Parte 2 - For
Ae! Pessoal!

Grande Final de semana! 100% de aprovação na faculdade! Enfim "férias"!

Bem vamos falar de Python então!

Hoje veremos o for.



Vamos começar com um exemplo simples:

l = [1,2,3,4,5]
for i in l:
    print i

Aqui, inicialmente, começamos com algo que ainda não vimos: listas.

Começamos criando l como uma lista que contém uma sequência de números.

Então, esta lista é usada dentro do for.


*** Nota para programadores de outra linguagem ***

Em outras linguagens, determinamos o valor inicial da variável contadora, seu limite e o passo de iteração. Em python isso não acontede. Aqui, o for somente itera sobre listas. Isto traz várias vantagens, como por exemplo, iterar sobre strings, ou listas de elementos variados.


Será mostrado adiante porque este for não está em desvantagem frente ao for das outras linguagens.


*** Fim da Nota ***

Então, a cada iteração, a variável de iteração, neste caso i, recebe uma posição da lista.

Assim, este trecho acima imprime na tela todos os valores contidos na lista l.

Vamos ver agora este trecho de código:

d = ['arroz', 'feijao', 'carne', 'batata']
for i in d:
    print 'Estou cozinhando ', i

Este exemplo demonstra a utilização do for com listas que contém strings, mostrando que pode-se usar listas com qualquer objeto num for.

No for também podemos usar break e continue. Assim, podemos controlar ainda mais o comportamento do laço. Além disso, há uma particularidade no for do Python que o deixa muito poderoso: podemos usar um else ao final do for como no exemplo a seguir:

for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    if i == 'd':
        break
    print i
else:
    print 'd'

Usando o else no final, podemos controlar o que será executado ao final de um execução completa do for e o que será executado se o laço for quebrado por um break. Quando o break quebra o laço, a execução segue pra dentro do else!

Neste exemplo, serão mostradas sempre as letras a, b, c e d, mas d não será impresso dentro do for, mas dentro do else!

Isto é muito importante, pois evita que tenhamos que fazer testes complicados para detectar quando um for for quebrado por um break que será chamado em condições complexas.

Finalmente, muitos devem estar se perguntando: "Como este for pode ser tão poderoso se temos que definir as listas manualmente?"

O fato é que não temos que fazer manualmente se for uma lista de números (assim como não precisamos em outras linguagens).

Existe uma função em Python, range, que retorna uma lista de números no intervalo especificado. Veja o exemplo:

for i in range(50):
    if i%2 == 0:
        print i, 'é par'
    else:
        print i, 'é impar'

Quando fazemos range(50), teremos uma lista de inteiros de 0 a 49. (experimente no shell).


Bem, pessoal! Por hoje é isso!

Espero que tenhm gostado! Agora falta pouco para iniciarmos uma programação efetiva em Python!

Nos Próximos Posts, tipos de dados nativos do Python!

Comentem!
Assinem o Feed e não percam nenhum post do Programe em Python!

Abraço!
Até  próxima!