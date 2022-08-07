Title: Tutorial de Git e Github
Date: 2022-08-07 10:02
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI, Git, GIthub
Slug: tutorial-git-1

Olá!

Eu estava escrevendo a continuação do tutorial de pelican quando percebi que para falar de github pages, primeiro é importante falar de git e github para ter certeza que estamos todos alinhados mais adiante.

Então, o que é GIT?

Git é um sistema de gerenciamento de versões de código, ou seja, ele é usado para controlarmos alterações no código e é especialmente útil quando trabalhamos em colaboração, seja num time centralizado ou de forma distribuída como acontece com projetos open source, por exemplo.

Vou deixar aqui a página oficial onde você pode ver como [instalar o GIT](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git). Se você usa Windows, recomendo que use `Git Bash`, que faz parte da instalaço oficial, para interagir com repositórios GIT.

Dado que agora você tem git instalado no seu computador, vamos configurar seu github.

Crie sua conta no [github](https://github.com), caso ainda não tenha.

No seu computador abra o terminal onde você usa o git. Vamos aqui gerar uma chave SSH para autenticar no github de forma segura. Entre o comando:

    ssh-keygen

Você pode simplesmente usar as opções padrão. Elas não são as mais seguras mas acredito que sejam suficientes para início de conversa. Se você prover uma senha para sua chave SSH, terá de usá-la sempre que for usar o acesso ao github no terminal, por exemplo.

Após executar este comando, você terá criado um par de arquivos na pasta `.ssh` na sua pasta de usuário. Estes sœ `id_rsa` e `id_rsa.pub`.

Vamos precisar do conteúdo do arquivo `id_rsa.pub`.

Agora, na sua página do gihub, clique no ícone do seu usuário (canto superior direito da página) e nas opções, selecione `Settings`.

![Github User Settings](/images/githubUserMenu.png)

Ali, em `Access` selecione `SSH and GPG keys`. Clique no botão `New SSH Key`.

![Github Add SSH](/images/githubAddSSH.png)

Copie o conteúdo do arquivo `id_rsa.pub` e cole em `Key`, Dê algum nome relevante e salve.

![Github Save SSH](/images/githubSaveKey.png)

Agora seu github está configurado.

Crie então um repositåorio no github atraves do botão `+` no canto superior direito ao lado do menu de usuário.

![Github cria repositório](/images/githubCriaRepo.png)

Você verá uma página com instruções de como clonar seu repositório. Selecione a opção SSH ecopie o link.

![Github clona Repo](/images/githubCloneRepo.png)

No terminal, gigite:

    git clone git@github.com:username/repositorui.git

Onde você vai substituir o `git@github.com:username/repositorui.git` pela URL que copiou do github. Ela deve ter este formato também, começando com `git@github.com`.

Entre na pasta criada e crie um arquivo, pode ter qualquer nome, como README.md por exemplo e escreva algo nele.

Agora você precisa informar ao git que ele deve guardar as mudanças deste repositório, então digite.

    git add .
    git commit -m "primeiro commit"

Agora vamos enviar este arquivo para o github com um comando de `push`.

    git push origin master

Pronto! Você deu seus primeiros passos com Git e Gihub!

Espero que tenham gostado e não esqueçam de deixar seuas opiniões e dúvidas nos comentários!

Até o próximo post!
