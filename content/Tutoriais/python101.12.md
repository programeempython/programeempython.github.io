Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-12
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Boa noite pessoal!

Que tal falarmos hoje sobre como criar e chamar funções no seu código Python?

Quem viu o tutorial de Como Fazer um Switch em Python viu ali como isto é feito, mas vamos analisar em mais detalhes.

Você sabe por que é importante usar funções num programa?

Imagine um trecho de programa que tenha que ser executado várias vezes durante a execução. O que é melhor: reescrever várias vezes a mesma coisa e criar um código imenso ou criar uma estrutura que execute este trecho sem necessidade de repeti-lo?

Com certeza, a segunda opção deixa o código menor, mais legível e mais organizado. Esta subdivisão de um programa mais complexo em partes menores é chamada modularização.

Vejamos então como usar as funções em Python!

Inicialmente, devemos saber que a palavra reservada def é quem indica que será definida uma função. Em seguida, damos o nome da função e especificamos os nomes dos parâmetros de entrada.

Estes parâmetros podem assumir várias formas como será visto neste post. Porém nunca são usados para retornar dados para o programa principal ou para a função chamante.

Isto quer dizer que a única forma de retornar dados no Python é através da instrução return.

Na verdade, isto não é uma desvantagem, visto que funções podem retornar tuplas contendo qualquer objeto.


#definindo funções

def soma(x, y):
    return x + y

def quadrado(x):
    return x*x
    
def soma_quadrado(x, y):
    x2 = quadrado(x)
    y2 = quadrado(y)
    return (x2, y2, soma(x2, y2))
  
Na função soma, são passados obrigatoriamente dois parâmetros e é retornada a soma dos dois. Esta função pode receber quaisquer objetos que suportem a operação de soma.

A função quadrado receba somente um parâmetro e retorna seu quadrado. Esta função se aplica somente a valores numéricos.

Já a função soma_quadrado recebe duas variáveis numéricas e retorna uma tupla contendo os quadrados das variáveis de entrada mais a soma desses quadrados.

Vejamos agora como chamar estas funções dentro do seu programa:


#chamando funções

soma(2, 2)
quadrado(3)
soma_quadrado(3, 4)

A primeira chamada retorna 4, a segunda 9 e a terceira (9, 16, 25). No lugar dos números poderiam ter sido usadas variáveis que contivessem estes valores.

Existem algumas características interessantes da passagem de parâmetros em Python. Veremos algumas a seguir.

Parâmetros com valor padrão

Funções com parâmetros com valor padrão podem receber um número variável de parâmetros na chamada, pois o valor padrão será assumido para o parâmetro omitido.

Sempre deixamos o parâmetro com valor padrão para o final da tupla na definição da função. Observe:

#parâmetros com valores padrão

def gosta_cachorros(op='sim'):
    if op == 'sim':
 print 'Eu gosto de cachorros'
    elif op == 'nao':
 print 'Eu nao gosto de cachorros'
    else:
 print 'Responda com sim ou nao'

Neste caso se chamássemos esta função no shell do python, ficaria assim:

>>> gosta_cachorros()
Eu gosto de cachorros
>>> gosta_cachorros('sim')
Eu gosto de cachorros
>>> gosta_cachorros('nao')
Eu gosto nao de cachorros
>>> gosta_cachorros('gato')
Responda com sim ou nao

Assim, se o parâmetro com valor padrão for omitido, o valor padrão será usado.

Um caso particular desta propriedade da passagem de parâmetros das funções é a utilização de vários argumentos com valores padrão. Estas são as funções com argumentos chave.

Veja um exemplo:

#argumentos chave
def gosta_de(acao='comer', objeto1 = 'batata frita', objeto2 = 'bife'):
    print 'Eu gosto de ', acao, ' ', objeto1, ' com ', objeto2

As chamadas a esta função podem ocorrer da seguinte maneira:

>>> gosta_de()
Eu gosto de comer batata frita com bife
>>> gosta_de(objeto1 = 'lasanha')
Eu gosto de comer lasanha com bife
>>> gosta_de(acao = 'cozinhar')
Eu gosto de cozinhar batata frita com bife
>>> gosta_de('beber', 'agua')
Eu gosto de beber agua com bife
>>> gosta_de('beber', 'suco de laranja', 'acerola')
Eu gosto de beber suco de laranja com acerola
>>> gosta_de('beber', objeto2 = 'agua')
Eu gosto de beber batata frita com agua
>>> gosta_de(1, 2, 3)
Eu gosto de 1 2 com 3

Os parâmetros passados vão para o argumento ao qual são atribuídos. Caso não haja atribuição, os valores serão atribuídos da esquerda para a direita, por isso a diferença entre gosta_de('beber', 'agua') e gosta_de('beber', objeto2 = 'agua').

Note na última chamada que esta função aceita qualquer tipo de dado que seja imprimível (suporte print)

Com estas informações, você já será capaz de começar a fazer suas próprias funções! Lembre-se que se a função não retorna nada o return pode ser omitido.

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!
