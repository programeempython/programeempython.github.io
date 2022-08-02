Title: Python 101 - Parte 4 - Estruturas Condicionais em Python, o Retorno
Date: 2022-08-02 22:06
Slug: python-101-parte-4
Category: Tutoriais
Tags: Tutorial, Python 101

Continuando o artigo sobre Estruturas Condicionais em Python, veremos agora algumas outras fomas de usar a construção `if`/`else`.

Se você ainda não viu o post anterior, veja aqui a introdução aos [Condicionais em Python](({filename}/Tutoriais/python101.3.md))

Muitas vezes, não é possível resolver um problema computacional simplesmente com um if/else. Então, usamos vários conjuntos de if/else aninhados (um dentro do outro)

    #!python
    caminho = 3
    if caminho == 0:
        print("Volte para a posicao inicial")
    else:
        if caminho == 1:
            print("Siga em frente")
        else:
            if caminho == 2:
                print("Abaixe a cabeca")
            else:
                if caminho == 3:
                    print("Você caiu no buraco")
                else:
                    print("Opcao invalida")

Mas, dá pra perceber que, se você tiver uma estrutura muito grade de condições, seu código vai ficar bem bagunçado... imagina trinta `if`/`else` aninhados dessa forma? Não dá!

Então, pra resolver este problema, temos a construção `if`/`elif`/`else`. O `elif` faz o papel das sequências de `else` que contém `if`. Veja como o código fica muito mais legível e organizado!

    #!python
    d = 4

    if d > 0:
        print("d é positivo")
    elif d < 0:
        print("d é negativo")
    else:
        print("d é nulo")


Você pode ter quantos `elif` forem necessários entre o `if` e o `else`. Veja este exemplo:

    #!python
    opcao = 2
    if opcao == 0:
        print "O valor escolhido foi 0"
    elif opcao == 1:
        print "O valor escolhido foi 1"
    elif opcao == 2:
        print "O valor escolhido foi 2"
    elif opcao == 3:
        print "O valor escolhido foi 3"
    else:
        print "O valor escolhido não é válido"

O código continua organizado e legível, ajudando no entendimento do programa!

Provavelmente, neste ponto, as pessoas que conhecem C, C++, java ou algumas outras linguagens devem estar se perguntando: Mas cadê o switch?

Na realidade, python não tem um switch como temos em outras linguagens, sendo que sua função é muito bem cumprida pelas estruturas 'if'/'elif'/'else'. Estas estruturas ainda tem vantagens sobre algumas implementações do switch que por exemplo somente fazem comparações de inteiros e caracteres únicos.

É possível simular um switch de forma muito eficiente e elegnte no Python, mas isto ficará para um próximo post com conteúdo mais avançado.

Vamos ficando por aqui.

No próximo tópico, falaremos de Estruturas de Repetição!

ão deixe de enviar dúvidas e opiniões nos comentários abaixo!

Até o próximo post!