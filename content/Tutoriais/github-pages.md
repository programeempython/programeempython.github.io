Title: Tutorial de Pelican com Github Pages e CircleCI - 2
Date: 2022-08-08 9:30
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI
Slug: tutorial-pelican-2

Olá!

Chegou a hora de continuarmos o tutorial de como publicar seu blog com Pelican, Github Pages e Circle CI como eu fiz, e caso você esteja chegando por aqui agora, confira nossos tutoriais anteriores

* [Tutorial Inicial de Pelican]({filename}/Tutoriais/pelican.md).
* [Tutorial básico de GIT e GitHub]({filename}/Tutoriais/git-github.md)

Hoje vamos falar sobre Github Pages.

Github Pages é uma funcionalidade gratuita do Github que te permite criar um site estático para seu perfil ou para seus projetos. Geralmente estes sites terão uma URL do tipo `usuario.github.io` ou `projeto.github.io`. Porém, é possível também colocar seu próprio domínio, como fiz aqui.

Para este tutorial, vamos usar o github pages para seu usuário, assim, crie um repositório chamado `username.github.io`, onde username é seu nome de usuário.

No canto superior direito do site clique no `+` e selecione `New Repository`. O nome deve ser na forma `username.github.io`, como disse acima. 

![New Repository Github](/images/githubAddRepo.png)

Agora, vamos clonar o repositório. Se você nunca usou git ou github antes, o [tutorial listado acima](({filename}/Tutoriais/git-github.md)) é essencial para continuar.

Copie o link SSH para clonar seu repositório, e execute o comando:

    git clone git@github.com:username/username.github.io

Isto vai criar uma pasta chamada `username.github.io`.

Entre na pasta, e vamos criar um arquivo chamado index.html, e este terá o seguinte conteúdo:

    #!html
    <html>
        <body>
            <h1>Olá! Github Pages é muito legal!</h1>
        </body>
    </html>

Em seguida vamos fazer commit e push deste arquivo para nosso repositório.

    git add .
    git commit -m "primeiro commit"
    git push origin main

Agora no github, na página do seu repositório, vamos clicar em `Settings`.

![Github Repository Settings](/images/gitHubRepoSetting.png)

No menu lateral, na sessão `Code and Automation` selecione `Pages`. Então, em `Branch` selecione `main`.

![Github repo settings pages](/images/githubsettingsbranch.png)

Clique no botão `Save`.

Aguarde um tempo, geralmente menos de 1 minuto, e sua página do Github Pages estará no ar! Muito fácil, não?

![Primeira página do Github Pages](/images/githubPagesFirst.png)

No próximo post vamos juntar Pelican e Github Pages e estaremos mais próximos de ter nosso blog pronto para publicar :D

Espero que tenham gostado e não esqueçam de deixar suas opiniões e dúvidas nos comentários!

Até o próximo post!