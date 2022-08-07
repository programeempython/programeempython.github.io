Title: Pelican Tutorial with Github Pages and CircleCI - 2
Date: 2022-08-08 9:30
Category: Tutoriais
Tags: Tutorial, Pelican, Github Pages, CircleCI
Slug: tutorial-pelican-2
Lang: en
Translation: true

Hello!

It's time for us to continue the tutorial on how to publish your blog with Pelican, Github Pages and Circle CI like I did, and in case you're getting here now, check out our previous tutorials

* [Starter Pelican Tutorial]({filename}/Tutoriais/en/pelican.md).
* [Basic GIT and GitHub Tutorial]({filename}/Tutoriais/en/git-github.md)

Today we are going to talk about Github Pages.

Github Pages is a free feature of Github that allows you to create a static website for your profile or projects. Usually these sites will have a URL like `user.github.io` or `project.github.io`. However, you can also put your own domain, as I did here.

For this tutorial, we're going to use github pages for your user, so create a repository called `username.github.io`, where username is your username.

In the upper right corner of the site click on the `+` and select `New Repository`. The name must be in the form `username.github.io`, as said above.

![New Github Repository](/images/githubAddRepo.png)

Now, let's clone the repository. If you've never used git or github before, the [tutorial listed above](({filename}/Tutoriais/en/git-github.md)) is essential to continue.

Copy the SSH link to clone your repository, and run the command:

    git clone git@github.com:username/username.github.io

This will create a folder called `username.github.io`.

Enter the folder, and we will create a file called index.html, and this will have the following content:

    #!html
    <html>
        <body>
            <h1>Hello! Github Pages is really cool!</h1>
        </body>
    </html>

Next we will commit and push this file to our repository.

    git add .
    git commit -m "first commit"
    git push origin main

Now on github, on your repository page, let's click on `Settings`.

![Github Repository Settings](/images/gitHubRepoSetting.png)

In the side menu, in the `Code and Automation` section select `Pages`. Then in `Branch` select `main`.

![Github repo settings pages](/images/githubsettingsbranch.png)

Click on the `Save` button.

Wait for a while, usually less than 1 minute, and your Github Pages page will be live! Very easy, no?

![First page of Github Pages](/images/githubPagesFirstEN.png)

In the next post we will join Pelican and Github Pages and we will be closer to having our blog ready to publish :D

I hope you liked it and don't forget to leave your opinions and questions in the comments!

See you in the next post!