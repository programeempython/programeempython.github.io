Title: Tutorial de Git e Github
Date: 2022-08-07 10:02
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI, Git, Github
Slug: tutorial-git-1
Summary: I was writing the next post to the pelican tutorial when I realized that in order to talk about github pages, it's important to first talk about git and github to make sure we're all on the same page later on.
Lang: en
Translation: true

Hi!

I was writing the next post to the pelican tutorial when I realized that in order to talk about github pages, it's important to first talk about git and github to make sure we're all on the same page later on.

So what is GIT?

Git is a code version management system, that means, it is used to control code changes and is especially useful when we work in collaboration, either in a centralized team or in a distributed way as with open source projects, for example.

I'll leave here the official page where you can see how to [install GIT](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git). If you use Windows, I recommend using `Git Bash`, which is part of the official package, to interact with GIT repositories.

Since you now have git installed on your computer, let's configure your github.

Create your account on [github](https://github.com) if you still don't have it.

On your computer open the terminal where you use git. Here we will generate an SSH key to authenticate to github securely. Enter the command:

    ssh-keygen

You can just use the default options. They are not the safest but I believe they are good enough to start using it. If you provide a password for your SSH key, you will have to use it whenever you use github access on the terminal, for example.

After running this command, you will have created a couple of files in the `.ssh` folder in your home folder. These are `id_rsa` and `id_rsa.pub`.

We will need the contents of the `id_rsa.pub` file.

Now, on your gihub page, click on your user icon (top right of the page) and from the options select `Settings`.

![Github User Settings](/images/githubUserMenu.png)

There, under `Access` select `SSH and GPG keys`. Click on the `New SSH Key` button.

![Github Add SSH](/images/githubAddSSH.png)

Copy the contents of the `id_rsa.pub` file and paste it in `Key`, Give it some relevant name and save.

![Github Save SSH](/images/githubSaveKey.png)

Now your github is set up.

Then create a repository on github via the `+` button in the upper right corner next to the user menu.

![Github creates repository](/images/githubCriaRepo.png)

You will see a page with instructions on how to clone your repository. Select the SSH option and copy the link.

![Github clones Repo](/images/githubCloneRepo.png)

In the terminal, type:

    git clone git@github.com:username/repositorui.git

Where you will replace `git@github.com:username/repositorui.git` with the URL you copied from github. It should have this format as well, starting with `git@github.com`.

Enter the created folder and create a file, it can have any name, like README.md for example and write something in it.

Now you need to tell git that it should save changes in this repository, so type.

    git add .
    git commit -m "first commit"

Now let's push this file to github with a `push` command.

    git push origin master

Done! You've taken your first steps with Git and Gihub!

I hope you liked it and don't forget to leave your opinions and questions in the comments!

See you in the next post!
