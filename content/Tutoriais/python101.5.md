Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-5
Category: Tutoriais
Tags: Tutorial, Python 101
Status: draft

Estruturas de Repetição Parte 1 - While
Olá Pessoal!

Ontem não tava muito legal não deu pra postar nada...

Mas vamos continuar falando sobre Programação Básica no Python!

Hoje vamos falar de uma das estruturas mais importantes: o while.



O while é um comando que manda um bloco de código ser executado enquanto uma condição não for satisfeita. Assim, permite que sejam criados loops de execução, assim como temos em jogos e aplicativos com interfaces gráficas.

O while é um comando muito útil, mas pode ser perigoso, pois se não tratarmos corretamente o critério de parada, o laço pode não ter fim, e o programa não faz o que deveria.

Vamos ver então um exemplo de como funciona o while em Python:

    x = 100
    while x > 0:
        print "x > 0"
        x = x - 1

Neste código, será mostrada a mensagem x > 0 até que x seja igual a zero. Quando o valor de x passar para 0, a verificação x>0 retornará falso, o programa sai do laço.

Vejamos agora este trecho de código:

    i = 0
    while True:
        print "Não vou parar nunca!"
        i = i + 1
        if i > 100:
            break

Aqui temos um laço que seria executado eternamente (while True:). Porém, dentro dele, fazemos uma verificação, e quando a variável i estiver guardando um valor maior que 100, será executado o comando break. O comando break literalmente quebra o laço, então, naquele instnte, o programa sai do laço.

Se logo abaixo deste código fizéssemos um print i, o valor impresso seria 100.

Assim, juntamente ao comando while, vimos agora o comando break que pode ser muito útil para quebrar laços fora da comparação padrão.

Vejamos agora o seguinte trecho:

    i= 0
    while i < 100:
        if i % 2 == 0:
            continue
        print i

Inicialmente, i recebe o valor 0, e é comparado com 100. Como 0 é menor que 100, o laço começa. Logo em seguida, temos uma comparação: if 1%2 == 0:. aqui verificamos se i é múltiplo de 2. Caso i seja múltiplo de dois, há um comando continue. continue faz com que esta iteração do laço termine e o programa passe para a próxima iteração. Desta forma, o programa ignora tudo o que está após o if.

No caso de i não sei múltiplo de 2, o programa não executa o continue, e imprime o valor de i na tela.

Se um continue estivesse fora do if, sempre o programa executaria este continue, e nunca seria executado o que há após ele. Assim, o continue controla a execussão do laço sem quebrá-lo.

Por enquanto é isso.

Nosso próximo post vai falar sobre a construção for.

Comentem!
Assinem o Feed, assim você não perde um post do Programe em Python!

Abraços!
Até a próxima!