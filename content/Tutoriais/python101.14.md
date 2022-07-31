Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-14
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

As Várias Faces do Python - Programação Orientada a Objetos
Olá pesoal!

Agora em período de aulas tá difícil escrever. Tudo na correria.

Hoje vamos falar sobre mais uma das várias facetas do python, sendo esta a principal. E esta não é a principal por ser mais usada ou por ser melhor, mas pois esta é a base da linguagem.

Vamos falar da Programação Orientada a Objetos em Python.
Pra quem ainda não o viu o post anterior, confira como funciona a Programação Procedural em Python!

Para falarmos de Orientação a Objetos em Python, primeiro precisamos entender ao menos superficialmente o que é a orientação a objetos.

A Orientação a Objetos é um paradigma da programação que busca representar computacionalmente a forma como vemos o mundo: objetos que possuem características e comportamentos.

Assim, programamos usando classes, que contém métodos (que definem o comportamento) e atributos (que definem as características), representando os objetos.

Por exemplo, vejamos a classe a seguir:

class Aviao:
    turbinas = 0
    poltronas = 0
    capacidade = 0
    status_motor = 'desligado'
    altitude = 0.0
    
    def ligar_motor(self):
        self.status_motor = 'ligado'

    def desligar_motor(self):
        self.status_motor = 'desligado'

    def sobe(self, incremento):
        self.altitude += incremento

    def desce(self, decremento):
        self.altitude -= incremento

Inicialmente fazemos a declaração da classe. Logo abaixo, são inicializados atributos da classe. Esta inicialização não é necessária, mas permite que você especifique quais os atributos do objeto antes de usá-los nos métodos.

Eu recomendo para quem está começando que faça esta inicialização dos atributos para controlar melhor o que há em cada classe.

Em seguida, são definidos os métodos (funções internas de uma classe/objeto que determinam seu comportamento). Note que dentro das classe passamos um parâmetro para os métodos que não passamos para as funções comuns.

Este parâmetro (self) permite que os atributos da classe sejam acessados tanto para leitura quanto para escrita de dentro dos métodos.

 Outro conceito importante da orientação a objetos é a herança.

Através dela, um objeto herda os atributos e métodos de ser objeto pai, por assim dizer, e implementa métodos e atributos próprios.

Vejamos um exemplo:

class Teco_teco(Aviao):
    
    def self.__init__(self):
        Aviao.__init__()

    def liga_helice(self):
        self.status_motor = 'lagado'
 
    def desliga_helice(self):
        self.status_motor = 'deslagado'

A classe acima estende a classe Aviao, definindo dois métodos que se utilizam de atributos da classe pai. Nesta classe, encontramos um novo método: __init__.

O método __init__ é o primeiro a ser executado quando se inicializa (instancia) uma classe. O __init__ é chamado às vezes de construtor devido à semelhança com os construtores da linguagem Java, por exemplo.

Uma diferença importante entre __init__ e um construtor é que este último é executado antes da classe ser instanciada e o __init__ depois.

É importante observar que o __init__ nesta classe é utilizado para inicializar a classe pai, chamando o __init__ da mesma.

Vejamos um exemplo agora com herança múltipla:

class Carro_voador(Carro, Aviao):
    posicao_asa = 'fechada'
    
    def __init__(self):
        Carro.__init__()
        Aviao.__init__()
 
    def decola(self):
        posicao_asa = 'aberta'
        acelera()
        posicao_flap = 'subir'
        transfere_tracao(roda, helice)
        
    def pousa(self):
        posicao_asa = 'aberta'
        acelera(reverso=True)
        posicao_flap = 'descer'
        transfere_tracao(helice, roda)
        freia() 

Veja como esta classe herda características de ambas classes, Carro e Aviao, assim como um carro voador herdaria as características de ambos veículos.

Todos estes exemplos de classes são simplificações com fins unicamente didáticos para exemplificar os conceitos.

Agora. Como instanciar uma classe? e como chamar um método ou usar um atributo?
Simples, veja:

>>> aviao = Aviao()
>>> print(aviao.status_motor)
desligado
>>> aviao.ligar_motor()
>>> print(aviao.status_motor)
ligado

Por hora, isto é suficiente para uma demonstração superficial da Programação Orientada a Objetos no Python

Nos próximos posts veremos outras facetas do Python. Não Percam!

Comente!
Assine o Feed e não perca nenhum post do Programe em Python!

Siga-nos no twitter @programepython e identi.ca @programeempython!

Abraços!

Até a próxima!
