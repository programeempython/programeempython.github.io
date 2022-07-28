Title: Porque Pelican
Date: 2022-07-25 22:03
Modified: 2022-07-28 01:52
Category: Blogging
Tags: Geral, Blogging
Lang: en
Translation: true

Hi!

I've been thinking about how and if I should restart blogging, and after a long brainstorm, here we are, and I think nothing could be better here than to talk a little about the thinking process of my decision to use Pelican hosted on Github Pages instead of any other platform.

So, I think we can start with a little timeline of my blog's history.

My first version of Programe em Python was hosted on Blogger. It was quite easy and practical at first, but, it wasn't that easy to customize the pages because it has some very specific things on it's HTML.

After that I migrated to a django solution running on RedHat's Openshift. I used to love it. It was 100% customizable, my texts wen't through exectly as I wanted them to be, but after a while, opeshift changed it's rules and I took to long to notice as I wasn't on the best of my moments at that time. In the end I had to make a backup in a hurry, ando unfortunately I couldnt go on with the blog after that.

Some time later I found out about Github Pages and pelican, and I took my changes, but it wasn't still a good moment for me and the project once again stalled.

Now, when I decided to blog again, I had to choose between going on with Github Pages + Pelican or to look for something else that would fit me as I wanted.

I had some decisive points to consider.vos.

* The blog is mostly a static content website and it would hardly ever need much more than a static site given that with Pelican it's quite easy to add new articles and pages.
* Git is something I use daily and I always recommend, besides that it would allow me to blog from basically anywhere. Also, I would have my posts in a version control system, and that can come in handy sometimes.
* Pelican is a nice piece of software, allowing me to add new posts easily throuhg git and using Markdown.

Some issues that I had to find workarounds for include the fact that Pelican is not natively supported by Github Pages like Jekyll for example, and to be able to have search and some other things I'd need Pelican plugins, increasing a bit the complexity of using it. But it wasn't enough to let me down.

One of the workarounds were the creation of a CircleCI workflow that generates the static site and commits to the proper branch of Github when I add a content to the work branch of the repo. This way, publishing the content wouldn't anymore depend on me running pelican commands locally.

One question you may ask is why I decided to use Pelican instead of Jekyll or Hugo for example?

My thought in that case was simple. I wanted a python software for that. So if I ever need to bugfix or improve something, I'll be working with the language I know the most.

Besides that, Pelican uses Jinja2 for then templates, and that's a library I have already used and it kind of resembles the Django template system too.

So, here we are. A blog using Pelican to generate the static site, hosted on Github Pages and CircleCI to automate the publishing of the posts when I push them.

I hope you enjoyed this little post. If you would like to know more about how Pelican works or how to create your own blog using this setup, let me know in the comments below!

See you in the next post!