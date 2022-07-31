Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-15
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

As Várias Faces do Python - Programação Funcional
Olá pessoal! Não tive como postar antes do final de semana, mas aqui estamos com mais Python pra vocês. Vamos falar agora sobre Programação Funcional em Python.


Pra quem ainda não viu os outros posts dobres as faces do python aqui estão:
Programação Procedural;
Programação Orientada a Objetos.
 Vamos agora então ao que interessa.

A programação funcional é um paradigma de programação que divide o problema em várias funções, sem que estas funções possuam estados internos que permitam a geração de resultados diferentes para várias execuções da mesma função para os mesmos parâmetros.

Assim, para a programação funcional, os resultados retornados por uma função devem depender unicamente dos parâmetros de entrada.

Sob certos aspectos, a programação funcional pode ser considerada o oposto da orientação a objetos, já que a primeira evita estados internos enquanto a segunda se baseia nas modificações dos estados internos dos objetos.

Abaixo são listados alguns motivos para se usar o paradigma funcional:

Os programas podem ser testados através de prova formal para comprovar que estão corretos;
Você é obrigado a quebrar seu problema em pequenos pedaços, sendo assim um paradigma que gera programas modularizados;
É mais fácil encontrar e corrigir erros (debugar o código);
Funções mais gerais podem ser reaproveitadas em muitas situações, como uma que receba o caminho para um arquivo e retorne seu conteúdo. assim, é possível escrever novos programas simplesmente reordenando algumas funções existentes e escrevendo as outras mais específicas do problema atual.

Dois grandes trunfos do Python para a programação funcional são os geradores e iteradores (generators e iterators), porém, devido à sua importância, estes merecem uma postagem específica.

Hoje, veremos funções que são ótimas ferramentas para a programação funcional. Estas são: lambda, map(), filter() e reduce().

lambda

lambda é uma palavra chave do python que é utilizada para definir pequenas funções anônimas. Esta é uma das características que o Python emprestou das linguagens funcionais mais famosas.

As expressões lambda somente permitem uma expressão, o que faz delas mais um recurso para deixar a sintaxe mais elegante.

Vejamos como usar:

>>> soma = lambda x, y : x + y
>>>soma(1, 2)
3

Muito simples, mas totalmente substituível por definições comuns de funções.

Um problema em utilizar funções lambda é que estas podem se tornar pouco ou nada inteligíveis caso alguém tente fazer algo muito complexo dentro delas.

Geralmente o ideal é definir uma função da forma tradicional.

filter()

Esta função recebe com parâmetros uma função e uma sequência (uma lista por exemplo), executando a função para cada elemento da sequência e retornando os elementos para os quais a função retorna verdadeiro.

Vejamos o seguinte exemplo

>>> #retornar os números primos entre 4 e 25
>>> filter(lambda x : x % 2 != 0 and x % 3 != 0, range(4, 25))
[5, 7, 11, 13, 17, 19, 23]

Como dito acima, uma função lambda maior pode se ternar difícil de entender, mas esta ainda é bem simples: retorna veradeiro se o número não for divisível por 2 nem por 3.

Assim, os números retornados são os primos entre 4 e 25.

Uma forma bastante útil de utilizar a função filter é para verificar a pertinência dos elementos de um grupo. Por exemplo:

>>> #verifica a existência de palavras que contém a letra z
>>> lista_sem_z = ['alface', 'camarão', 'ameixa', 'zebra']
>>> result = filter(lambda x : 'z' in x, lista_sem_z)
>>>if len(result) > 0:
...    print 'A(s) palavra(s)', reult, 'não deveria(m) estar aqui'
...
A(s) palavra(s) ['zebra'] não deveria(m) estar aqui

map()

Esta função recebe como parâmetros uma função e uma sequência assim como a filter(), porém, esta retorna uma lista com o resultado da função calculada sobre cada elemento da sequência.

Veja as seguintes situações:

>>> cubo = lambda x : x*x*x
>>> map(cubo, range(7))
[0, 1, 8, 27, 64, 125, 216]
>>> soma = lambda x, y : x + y
>>> map(soma, range(3), range(1, 4))
[1, 3, 5]

reduce()

Esta função, por sua vez, recebe os mesmos parâmetros que as duas anteriores, porém retorna um único valor, calculado a partir de uma função de dois argumentos da seguinte forma:
Calcula a função sobre os dois primeiros elementos da sequência;
Calcula a função sobre o resultado e o valor seguinte, assim, sucessivamente.
Vejamos  exemplos:

>>> reduce(lambda x, y : x + y, range(11))
55
>>> reduce(lambda x, y : x * y, range(1, 4))
6

Isto conclui a apresentação destas ferramentas de programação funcional da linguagem Python.

Espero que tenha gostado!

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!

Até a próxima!