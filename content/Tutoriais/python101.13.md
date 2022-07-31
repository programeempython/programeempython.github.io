Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-13
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Boa noite pessoal!

Após uma semana sem escrever, vamos avançar mais um pouco em nossa caminhada da programação Pyhton.

Aproveito para pedir desculpas aos leitores pela demora, já que twittei de tarde que o post sairia ainda no dia 10.

Hoje iniciaremos uma série de posts sobre as várias facetas desta linguagem tão versátil.

Vamos começar falando da primeira e mais simples pra quem está começando: Python como Linguagem Procedural.

Na maioria das vezes, as linguagens procedurais também são imperativas.


Mas não, você não precisa gritar com o computador, ou ser rígido.

Linguagem imperativa, significa que o computador faz o que você manda.

Você não representa objetos, não declara fatos... simplesmente manda e o computador faz.

Vamos então começar com a programação imperativa/procedural.

Python se encaixa mais como linguagem procedural que imperativa, mas pode ser usado para os dois fins.

Mas o que é  linguagem procedural então?

De forma geral uma linguagem procedural é uma linguagem imperativa que permite a criação de procedimentos, ou seja, trechos de código que podem ser executados em vários pontos do programa sem que seja necessário escrever tudo todas as vezes.

A Linguagem procedural está bem próxima de tudo o que foi demostrado nos posts até agora.

Vejamos um pequeno exemplo:

#! /usr/bin/env python
# -*- coding:utf8 -*-

'''
Programa para inverter uma matriz em python 2.x
'''

def le_dados():
    dado_lido = None
    matriz = []
    while True:
 dado_lido = raw_input('Digite uma linha da matriz. Para finalizar digite 0')
 if dado_lido == '0':
     break
 matriz.append(list(eval(dado_lido)))
    for linha in matriz[1:]:
 if len(linha) != len(matriz[0]):
     return -1
    return matriz
 
def inverte_matriz(matriz):
    return zip(*matriz)
    
def mostra_matriz(matriz):
    for linha in matriz:
 for elemento in linha:
     print '%d\t' % elemento,
 print '\n'
 
if __name__ == '__main__':
    matriz = le_dados()
    if matriz == -1:
 print 'Matriz não contem dados válidos. Terminando...'
 exit()
    print '\nMatriz Orginal\n'
    mostra_matriz(matriz)
    matriz = inverte_matriz(matriz)
    print '\nMatriz Transposta\n'
    mostra_matriz(matriz)

Este é um programa completo que lê dados de uma matriz digitada linha a linha pelo usuário e retorna matriz transposta. Vejamos em detalhes o que há neste programa:

Inicialmente, definimos a função que lê dados. Usamos um laço infinito que irá perguntar continuamente ao usuário pelos dados da matriz até que seja passado um 0 sozinho para o programa.

Em matriz.append(list(eval(dado_lido))) inserimos uma linha na matriz contendo uma lista resultante da avaliação da string digitada. Assim, se o usuário não digitar uma sequência de números separados por vírgulas, não será gerada a  lista, mas sim será levantado um erro.

Se você não está entendendo algo do que foi feito neste código, tente reler os posts anteriores, e voltar a este código. Caso alguma dúvida persista, deixe um comentário ou mande uma mensagem através da página de contato.

Após a aplicação perceber que o usuário digitou todos os dados da matriz, este confere se todas as linhas da matriz contém o mesmo número de elementos. No for é usado um recurso das listas chamado slicing, que permite fatiar a lista. neste caso, matriz[1:] significa, todas as linhas da matriz a partir da número 1.

Caso os dados estejam corretos é retornada a matriz. Do contrário, é retornado -1 para indicar o erro.

Passando para a outra função, usamos a função zip para transpor a matriz. a função recebe a matriz decomposta em linhas *matriz e reagrupa os dados segundo suas posições nas  listas passadas, assim todos os dados da primeira coluna vão pra primeira linha, os da segunda coluna pra segunda linha, etc.

Finalmente, na última função, imprimimos na tela os dados da matriz. Aí usei um recurso de formatação de dados no print que ainda não havia mostrado a vocês.

A seguir, encontramos um if que fará com que o código que encontramos a seguir não seja executado ao importarmos este programa em outro lugar.

Assim, este programa será executado somente como progama principal.

No código dentro do if chamamos as funções definidas acima para ler a matriz, invertê-la e mostrar a matriz antes e após a inversão.

Um detalhe que devemos considerar é que geralmente em Python, definimos todas as funções antes de criar o código principal do aplicativo.

Assim, espero que esta tenha sido uma boa demonstração da programação imperativa/procedural em Python.

Nos próximos posts veremos outras facetas do Python. Não Percam!

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!

Até a próxima!