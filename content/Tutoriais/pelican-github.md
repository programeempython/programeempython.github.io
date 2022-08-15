Title: Tutorial de Pelican com Github Pages e CircleCI - 3
Date: 2022-08-15 9:30
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI
Slug: tutorial-pelican-3

Olá!

Hora de continuar nosso tutorial e colocarmos nosso blog Pelican no github pages!

Caso você ainda não tenha visto os posts anteriores, veja aqui para podermos seguir do mesmo ponto.

* [Tutorial Inicial de Pelican]({filename}/Tutoriais/pelican.md).
* [Tutorial básico de GIT e GitHub]({filename}/Tutoriais/git-github.md)
* [Tutorial de Github Pages]({filename}/Tutoriais/github-pages.md)

Recapitulando rapidamente, no primeiro tutorial nós criamos um site bem simples com Pelican e no terceiro nós criamos uma página bastante simples no github pages.

A estrutura atual do seu diretório do github pages deve ser algo como

    usuario.github.io/
        index.html
    
Bom, não vamos usar este arquivo html.

No terminal, vamos criar uma nova branch, que será nossa branch principal para criarmos todos os textos do blog. 

    git checkout -b pelican

Este comando criará uma nova branch no seu repositório git local e vai automaticamente mudar a branch atual para `pelican`.

Vamos apagar o arquivo html.

    rm index.html

E agora vamos criar nosso blog. Precisamos ter acesso aqui ao comando `pelican-quickstart` que usamos no tutorial de pelican, então, num ambiente que contenha o pelican (pode ser o mesmo que usamos no tutorial de pelican), digite o comando:

    pelican-quickstart

Desta vez não vamos ficar nos parâmetros padrão. Adapte as escolhas que eu mostrar a seguir ao seu projeto.

    > Where do you want to create your new web site? [.]
    # Simplesmente aperte `Enter` para usar a opção padrão.
    > What will be the title of this web site? 
    # Caso tenha um nome para o blog, ele vai aqui, senão, usuario.github.io pode ser uma boa
    > Who will be the author of this web site?
    # Aqui, será seu nome
    > What will be the default language of this web site? [pt]
    # `pt` não é uma opção válida, então use `pt_BR`
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n)
    # Aqui responda `y` e depois a url do seu blog (https://usuario.github.io por exemplo
    > Do you want to enable article pagination? (Y/n)
    # Sempre acho uma boa ideia ter paginação, então, `Y`
    > How many articles per page do you want? [10]
    # Aqui também recomendo o padro, `Enter`
    > What is your time zone? [America/Sao_Paulo] 
    # Use aqui o que fizer mais sentido pra você
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n)
    # Esta é a parte mais importante. A resposta aqui é SIM! `Y`
    > Do you want to upload your website using FTP? (y/N) 
    # Nós não queremos, então `n`
    > Do you want to upload your website using SSH? (y/N) 
    # Mesmo aqui, `n`
    > Do you want to upload your website using Dropbox? (y/N) 
    # Aqui, `n`
    > Do you want to upload your website using S3? (y/N)
    # Aqui, `n'
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    #E aqui, `n`
    > Do you want to upload your website using GitHub Pages? (y/N)
    # Nós queremos usar github pages então a resposta aqui é `y`
    > Is this your personal page (username.github.io)? (y/N) 
    # E sim, é a página pessoal, então, `y`


Vamos precisar da lib de Python que interage com github pages então vamos instalá-la:

    pip install ghp-import

Para o caso de precisarmos editar este repositório em outro local, outro ambiente, vamos criar um arquivo `requirements.txt` que vai conter

    ghp-import
    pelican[markdown]

Isto nos permite instalar facilmente as dependências no futuro com o comando

    pip install -r requirements.txt

Mais uma vez você deve ter uma estrutura de arquivos dentro do seu repositório parecida com isto:

    content/
    pelicanconf.py
    publishconf.py
    requirements.txt

Vamos dar uma olhada no arquivo pelicanconf.py

    #!python
    AUTHOR = 'Author Name'
    SITENAME = 'My Blog'
    SITEURL = ''

    PATH = 'content'

    TIMEZONE = 'America/Sao_Paulo'

    DEFAULT_LANG = 'pt'

    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None

    # Blogroll
    LINKS = (('Pelican', 'https://getpelican.com/'),
            ('Python.org', 'https://www.python.org/'),
            ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
            ('You can modify those links in your config file', '#'),)

    # Social widget
    SOCIAL = (('You can add links in your config file', '#'),
            ('Another social link', '#'),)

    DEFAULT_PAGINATION = 10

    # Uncomment following line if you want document-relative URLs when developing
    #RELATIVE_URLS = True

Podemos remover os links e acrescentar links mais relevantes. Também podemos acrescentar links para redes sociais.

Vamos acrescentar uma URL para quando estivermos rodando o blog em modo de desenvolvimento para vermos como está o post, por exemplo.

Em `SITEURL` insira `'http://localhost:8000'`.

Agora vamos criar um post em content e podemos chamar por exemplo de `primeiro-post.md`

Sua estrutura de arquivos ficará

    content/
        primeiro-post.md
    pelicanconf.py
    publishconf.py
    requirements.txt

Em `primeiro-post.md` escreva:

    Title: Primeiro Post
    Date: 2022-08-14 12:30
    Category: Geral
    Tags: Geral
    Slug: primeiro-post

    # Olá!

    Este é meu primeiro post

    Isto é um [link](#)

    É muito __fácil__ criar posts com _Pelican_!


Aqui temos a estrutura de um post bem simples, com metadados básicos e um exemplo de texto que exemplifica algumas marcações do Markdown.

Vamos testá-lo no servidor de testes.

    pelican -l -r
    --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
    Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop
    [04:22:41] WARNING  Watched path does not exist: /path/to/username.github.io/content/images


    -> Modified: settings, content, theme. re-generating...
    Done: Processed 1 article, 0 drafts, 0 hidden articles, 0 pages, 0 hidden pages and 0 draft pages in 0.06 seconds.

Acesse [o servidor local](http://localhost:8000) e você deve ver algo assim:

![Server local](/images/pelican-blog-first.png)

Para continuarmos, você precisa ter instalado o `make`. Como no Windows a instalação do make é mais chatinha, segue um [tutorial de make no Windows](https://coffops.com/usando-comando-make-projetos-windows/).

Podemos usar o make para várias tarefas.

Para executar um servidor de desenvolvimento, podemos usar

    make devserver

Podemos simplesmente gerar os arquivos para deploy com

    make publish

E para enviarmos para o github, vamos usar:

    make github

Porém, antes de enviarmos nosso projeto para o github pages vamos conferir a configuração do blog para publicação. Abra o arquivo `publishconf.py`. Ele deve ter aproximadamente este conteúdo:

    #!python
    # This file is only used if you use `make publish` or
    # explicitly specify it as your config file.

    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *

    # If your site is available via HTTPS, make sure SITEURL begins with https://
    SITEURL = 'https://jcempython.github.io'
    RELATIVE_URLS = False

    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

    DELETE_OUTPUT_DIRECTORY = True

    # Following items are often useful when publishing

    #DISQUS_SITENAME = ""
    #GOOGLE_ANALYTICS = ""

Em alguns instantes você poderá acessar seu site `usuario.github.io` e ver seu blog no ar!

Quando escrever novos posts, simplesmente execute `make publish` e `make github` e em alguns instantes seu post estará no ar!

Por hora é isto! Tenho certeza que você já vai se divertir muito com seu blog e já vai poder começar a postar tudo que quiser!

Não se esqueça, quando terminar de fazer alterações no seu blog, de fazer um commit das alterações para a branch pelican também.

    git add .
    git commit -m "uma mensagem do que foi feito"
    git push origin pelican

Assim você não corre o risco de perder suas alterações e tem sempre controle sobre as versões dos textos que vau publicar!

No próximo post vamos dar um tapa neste blog para termos mais funções, como comentários, por exemplo.

Espero que tenham gostado e não esqueçam de deixar suas opiniões e dúvidas nos comentários!

Até o próximo post!
