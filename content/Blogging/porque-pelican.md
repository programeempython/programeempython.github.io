Title: Porque Pelican
Date: 2022-07-25 22:03
Category: Blogging
Tags: Geral, Blogging
Summary: Aqui vou apresentar alguma razões para eu ter escolhido publicar meu blog com Pelican.

Olá!

Eu andei avaliando se e como eu deveria retomar o blog, e depois de muitas ideias, aqui estamos, e acho que nada como começar falando um pouco sobre o processo de decisão para escolher fazer o blog em Pelican hospedado no Github Pages ao invés de qualquer outra plataforma.

Para isto acho que podemos começar com um pequeno histórico do blog.

Minha primeira versão do Programe em Python foi no Blogger. Era bastante fácil e prático de início, porém, para customizar as páginas era um tanto trabalhoso devido às especificidades dos templates HTML do Blogger.

Depois, migrei para uma solução django rodando no openshift da redhat. Eu adorava. 100% customizavel, meus textos saiam bem como eu queria, mas depois de um tempo, o openshift teve mudanças pras quais eu demorei pra me atentar e tive que fazer um backup super corrido dos textos e infelizmente não consegui mais continuar com o blog.

Um tempo depois eu descobri github pages e pelican e fiz uma tentativa inicial, mas não estava num bom momento e o projeto mais uma vez não foi pra frente.

Agora, quando decidi retomar o blog tive que escolher entre continuar usando github pages e pelican ou procurar uma nova plataforma.

Minha escolha teve alguns pontos decisivos.

* O blog é um site estático e dificilmente vou precisar de muito mais do que um site estático pode me oferecer, dado que o Pelican simplifica muito a postagem dos textos e acrescentar as páginas.
* Git é um sistema que eu uso diariamente e que eu sempre recomendo, além de permitir versionamento dos texto, o que pode ser bastante útil, eu posso escrever de basicamente qualquer lugar e enviar facilmente para o github.
* Pelican é um gerador de sites estáticos, que me permite facilmente acrescentar novos posts ao blog, escrevendo com Markdown


Alguns pontos precisei levar em consideração são que o Pelican não tem um suporte nativo no Github Pages como tem o Jekyll por exemplo, e para ter busca e outras features, precisei de alguns plugins do pelican. Isto aumenta um pouco as complexidades, porém não o suficiente para me desanimar.

Algo que eu fiz também foi implementar um workflow no CircleCI para publicar a postagem quando eu fizer um commit na branch do blog, assim, a publicação que dependeria de eu rodar alguns comandos do pelican fica automatizada.

Uma pergunta que pode ficar é, por que usei Pelican no lugar de Jekyll ou Hugo por exemplo?

Minha ideia neste sentido foi bem simples. Eu queria um gerador de site estático feito em Python. Assim, se eu eu sentir que preciso de algo ou que tem um bug eu posso trabalhar na mudança facilmente.

Também, Pelican usa Jinja2 para os templates, e esta biblioteca eu já usei diversas vezes, além de ser parecida com a biblioteca de templates do Django.

Assim, aqui estamos. Um blog usando Pelican para gerar o site, o host sendo o sistema de pages do github, e com CircleCI automatizando as publicações quando eu envio os posts.

Espero que tenham gostado. Quer saber mais sobre como funciona o Pelican, ou como criar seu próprio blog usando esta stack?

Deixe seu comentário!

Abraço!