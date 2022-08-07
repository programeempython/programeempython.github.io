Title: Tutorial de Pelican com Github Pages e CircleCI - 1
Date: 2022-07-31 22:03
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI
Slug: tutorial-pelican

Olá!

Como prometido, vamos abordar como criei meu blog com Pelican, Github Pages e CircleCI num tutorial. Como é bastante conteúdo vamos dividir em partes e aqui veremos uma introdução ao Pelican.

Recapitulando, Pelican é um gerador de site estático, ou seja, gera um site estático em HTML baseado em conteúdos escritos numa linguagem de Markup, geralmente rich text ou markdown. Pelican gera as postagens usando Jinja2 como biblioteca de template. Assim, se você tem alguma familiaridade com jinja ou Django, que tem uma biblioteca de templates semelhante, você não vai ter dificuldades em por exemplo criar ou customizar temas para o Pelican.

Primeiro, para criar um site com Pelican, vamos instalá-lo.

Pode ser num ambiente virtual ou diretamente na sua instalação padrão do python. No terminal, execute:

    pip install pelican[markdown]

Isto vai instalar o Pelican com suporte a Markdown, que é minha linguagem de markup preferida.

Finalizando sua instalação, vamos criar um site Pelican.

Crie uma pasta onde ficará seu site, para executarmos comandos lá de dentro. No Linux, seria algo assim:

    mkdir ~/projetos/meu_blog/ -p
    cd ~/projetos/meu_blog

Então, agora vamos executar um comando do Pelican que vai iniciar nosso blog.

    pelican-quickstart

Este script vai te perguntar diversas coisas. 

    > Where do you want to create your new web site? [.] 
    > What will be the title of this web site? 
    > Who will be the author of this web site? 
    > What will be the default language of this web site? [pt] 
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n)
    > Do you want to enable article pagination? (Y/n)
    > What is your time zone? [America/Sao_Paulo] 
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n)

Vamos nos manter no mais simples possível para este tutorial introdutório, então responda

    (Somente digite `Enter`)
    Teste
    Teste
    (Somente digite `Enter`)
    n
    n
    (Somente digite `Enter`)
    n

Assim, o Pelican vai criar um projeto bastante simplificado que podemos usar para iniciar nosso blog. Num próximo post, vamos executar novamente este comando para criar realmente o blog que vamos publicar, mas aqui como é somente para introduzir o Pelican vamos manter a simplicidade.

Agora vamos criar nosso primeiro post exemplo. Veja que o Pelican criou uma estrutura de arquivos assim na pasta do blog:

    content/
    pelicanconf.py
    publishconf.py

Dentro da pasta content, crie um arquivo, vamos chamá-lo de teste.md (Muito criativo :p). Nele insira o seguinte conteúdo

    Title: Teste
    Date: 2022-07-31 08:00
    Category: Geral

    Olá! Este é meu primeiro post com Pelican!

Isto é o suficiente para um post com Pelican. Título, data, categoria e o conteúdo em si.

Agora vamos rodar um servidor de teste e ver o que nosso blog.

    pelican -r -l

O resultado deve ser algo assim:

      --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---
    Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop
    [22:56:36] WARNING  Docutils has no localization for 'pt'. Using 'en' instead.                                                                                                                                                                                                                                       log.py:91
            WARNING  Watched path does not exist: /home/jcemelanda/projetos/myblog/content/images                                                                                                                                                                                                                     log.py:91

    -> Modified: settings, content, theme. re-generating...
    Done: Processed 1 article, 0 drafts, 0 hidden articles, 0 pages, 0 hidden pages and 0 draft pages in 0.06 seconds.

Acesse o endereço indicado `http://127.0.0.1:8000`

![Screenshot Pelican 001](/images/pelican-tut-001.png)

Esta deve ser a aparência do seu blog.

Agora abra seu arquivo `pelicanconf.py`. Seu conteúdo deve ser aproximadamente este:

    AUTHOR = 'teste'
    SITENAME = 'TESTE'
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

    DEFAULT_PAGINATION = False

    # Uncomment following line if you want document-relative URLs when developing
    #RELATIVE_URLS = True

Este arquivo é bem autoexplicativo. Aqui é nele que mexemos para a maioria das configurações do Pelican.

Finalmente, abra o `publishconf.py`. Seu conteúdo deve ser aproximadamente este:

    # This file is only used if you use `make publish` or
    # explicitly specify it as your config file.

    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *

    # If your site is available via HTTPS, make sure SITEURL begins with https://
    SITEURL = ''
    RELATIVE_URLS = False

    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

    DELETE_OUTPUT_DIRECTORY = True

    # Following items are often useful when publishing

    #DISQUS_SITENAME = ""
    #GOOGLE_ANALYTICS = ""

Veja que este arquivo importa de pelicanconf, logo, aqui você consegue sobrescrever configurações, te permitindo ter uma configuração para seu ambiente onde escreve os posts e outra para a efetiva publicação do site.

No momento, estas informações são suficientes para prosseguirmos, então, não perca a próxima parte deste tutorial onde vamos falar sobre Github pages para depois juntarmos as duas coisas :D

Espero que tenham gostado e não esqueçam de deixar seuas opiniões e dúvidas nos comentários!

Até o próximo post!