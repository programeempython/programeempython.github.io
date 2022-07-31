Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-7
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Dados em Python
Olá pessoal!

Hoje vamos ver uma coisa muito importante no Python: as estruturas de dados nativas.

São vários os tipos de dados nativos do Python. Entre eles, os mais importantes, pois são essenciais para qualquer programa, são os tipos:
inteiro
ponto flutuante
cadeia de caracteres


O Inteiro representa os números inteiros, o ponto flutuante é usado para representar números decimais, e a cadeia de caracteres para representação de texto.

Porém, em Python, diferente de outras linguagens, estes tipos de dados, assim como todas as outras estruturas da linguagem são objetos, desta forma, o tipo básico de tudo em python é object. Há muito a se discutir sobre tipos de dados, mas para efeito de simplificação consideraremos assim.

Desta forma, cada classe que se cria em Python é um novo objeto, e assim também um novo tipo.

Voltando às estruturas de dados nativas, veremos que estas são conjuntos estruturados de objetos que podem conter elementos de qualquer outro tipo.

A primeira e talvez mais largamente usada destas estruturas é a list. Uma list implementa uma lista que pode conter virtualmente qualquer objeto, sendo composta por quantos tipos de objeto for necessário (diferente de algumas linguagens).

Desta forma,  listas se tornam uma ferramenta muito poderosa dentro do Python. Teremos mais adiante um post focado especialmente nas listas e seus métodos.

Para criar uma lista, basta atribuir valores a ela da seguinte forma:

l = [1,2,3,4,5]

Assim como fizemos quando vimos como funciona o for.

Outra estrutura de dados muito importante e largamente usada é a tuple (tupla). Tuplas contém conjuntos de valores assim como as listas, porém se diferenciam destas principalmente pelo fato de as tuplas não poderem ser alteradas após sua criação, e as listas sim.

Vamos criar uma tupla:

t = (1,2,3,4,5)

As tupals são as estruturas que a linguagem usa para passar parâmetros para funções (mais detalhes num post específico).

Por exemplo, a função range, aceita valor inicial, valor final e passo. Estão, ao chamar no shell:

>>> range(1, 6, 2)
[1, 3, 5]

Os valores (1, 6, 2) são enviados para a função como uma tupla.

Vejamos agora uma das estruturas de dados mais poderosas do Python, e que possui muitas possibilidades de utilização. Esta estrutura é o dict (dicionário) que relaciona pares de chave e valor.

Assim criamos um dicionário:

d = {'a':1, 'b':2,'c':3, 'd':4, 'e':5}

Finalmente, a última estrutura de dados nativa do Python que veremos hoje é o set (conjunto). Os sets tem um uso muito especial. Este comando cria listas a partir de uma lista, onde não há elementos repetidos.

Por exemplo, ao criar este set:

s = set([1, 1, 2, 3, 5, 7, 13, 17])

Neste caso, o conjunto será [1, 2, 3, 5, 7, 13, 17], pois 1 aparecia 2 vezes na lista original, e no set ele aparece somente uma vez.

Isto é muito útil, por exemplo, para saber, numa lista de números muito grande, quais são os números que aparecem, desconsiderando as repetições.

Nos Próximos posts, apresentrei cada uma destas estruturas em detalhes.

Comentem!
Assinem o Feed, e não percam nenhum posto do Programe em Python!

Abraços!
Até a próxima!

P.S. Atenção pessoal! A Partir desta semana começo a falar sobre assuntos mais avançados da linguagem! Aguardem!