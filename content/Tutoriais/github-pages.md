Title: Tutorial de Pelican com Github Pages e CircleCI - 2
Date: 2022-08-03 19:30
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI
Slug: tutorial-pelican-2
Summary: Github Pages é uma funcionalidade gratuita do Github que te permite criar um site estático para seu perfil ou para seus projetos. Geralmente estes sites terão uma URL do tipo `usuario.github.io` ou `projeto.github.io`. Porém, é possível também colocar seu próprio domínio, como fiz aqui.
Status: draft

Olá!

Chegou a hora de continuarmos o tutorial de como publicar seu blog com Pelican, Github Pages e Circle CI como eu fiz, e caso você esteja chegando por aqui agora, confira nosso [Tutorial Inicial de Pelican]({filename}/Tutoriais/github-pages.md).

Hoje vamos falar sobre Github Pages.

Github Pages é uma funcionalidade gratuita do Github que te permite criar um site estático para seu perfil ou para seus projetos. Geralmente estes sites terão uma URL do tipo `usuario.github.io` ou `projeto.github.io`. Porém, é possível também colocar seu próprio domínio, como fiz aqui.

Para este tutorial, vamos usar o github pages para seu usuário, assim, crie um repositório chamado `username.github.io`, onde username é seu nome de usuário.

No canto superior direito do site clique no `+` e selecione `New Repository`. O nome deve ser `username.github.io`, como disse acima. 

Agora, vamos clonar o repositório. Para isto, precisamos ter instalado o `git`.

Se você não tem GIT instalado, você precisará instalá-lo agora.

Para isto, recomendo este [Tutorial de Instalação do GIT](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git).

Após instalar o `git`, abra um terminal para podermos clonar o projeto.

Se você já está habituado com isto será bem simples, senão, recomendo que utilize o link https para clonar, já que implica em menos complexidade de configuração no momento.

Escolha uma pasta onde ficará seu projeto e execute dentro dela o seguinte comando:

    git clone https://github.com/jcempython/jcempython.github.io.git

O git vai pedir seu usuário e sua senha do github para clonar o repositório.

Com seu repositório criado, clique em Settings para podermos configurar o site. No menu lateral, na sessão `Code and Automation` selecione `Pages`. 