Title: Python 101 - Primeira Parte
Date: 2022-07-29 01:06
Category: Tutoriais
Tags: Tutorial, Python 101
Slug: python-101-parte-1

Bom, um blog com o nome Programe em Python não pode ficar sem um tutorial básico de Python, né?

Antes de mais nada, se você usa Linux ou MacOS você provavelmente já tem o Python então você está com sorte.

No windows, vá à [página de downloads do Python](https://www.python.org/downloads/) e baixe dali a versão mais recente.

![Download Python](/images/download-python.png)

Quando terminar o download, execute o instalador e siga as instruções de instalação.

Lembre-se de marcar a opção para inserir Python nos caminhos do sistema (*Add Python to PATH*), pois isto vai facilitar muito a sua vida.

Quando o Python estiver finalmente instalado, numa janela de linha de comando, (CMD ou powershell no Windows) digite Python e você deve ver algo semelhante a isto.

![Terminal Python](/images/python-terminal.png)

Veja que na primeira linha você consegue ver qual a versão do Python, e na última linha há um prompt esperando pelos seus comandos. 

    >>>

Este prompt será usado neste blog sempre para denotar que devemos escrever código no console do Python.

Faça um teste. Digite, seguido de `ENTER`:

    >>> print('Olá Mundo!')

O resultado deve ser algo assim:

    >>> print('Olá Mundo!')
    Olá Mundo!

Isto significa que o console do Python já te retorna as respostas para os comando logo em seguida de você executá-los. Veja por exemplo:

    >>> 23*256/98+3
    63.08163265306123

Finalmente, quando formos executar códigos com blocos, como `if` por exemplo, será assim:

    >>> if(True):
    ...     print('É verdade!')
    ...
    É verdade!

Assim, note que os 3 pontos `...` são indicadores de bloco de código no terminal do Python, ou seja, indicam que um comando iniciado acima ainda não foi terminado. Desta forma, precisamos inserir uma linha em branco para o Python perceber que finalizamos aquele comando e ele pode então executá-lo.

Acho que este é um bom momento para finalizarmos esta primeira parte do tutorial :D

Não deixem de **comentar** abaixo com sua opinião e dúvidas!

Até o próximo post!