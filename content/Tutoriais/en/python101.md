Title: Python 101 - First Part
Date: 2022-07-29 01:06
Slug: python-101-parte-1
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true
Summary: Well, a blog with the name Programe em Python can'e exist without a basic Python Tutorial, right?


Well, a blog with the name Programe em Python can'e exist without a basic Python Tutorial, right?

First things first, if you are using Linux or OSX you most probably already have Python installed, so you are a lucky person ;)

On windows, go to the [Python downloads page](https://www.python.org/downloads/) and download the most recent version from there.

![Download Python](/images/download-python.png)

When the download is complete, run the installer and follow the installation instructions.

Remember to check the option to insert Python in the system paths (*Add Python to PATH*), as this will make your life a lot easier.

When Python is finally installed, in a command line window (CMD or powershell on Windows) type Python and you should see something similar to this.

![Python Terminal](/images/python-terminal.png)

See that on the first line you can see the version of Python, and on the last line there is a prompt waiting for your commands.

    >>>

This prompt will be used throughout this blog to denote that we must write code in the Python console.
Try it. Type, followed by `ENTER`:

    >>> print('Hello World!')

The result should be something like this:

    >>> print('Hello World!')
    Hello World!

This means that the Python console already returns the answers to the commands right after you execute them. See for example:

    >>> 23*256/98+3
    63.08163265306123

Finally, when we run code with blocks, like `if` for example, it will look like this:

    >>> if(True):
    ... print('It's true!')
    ...
    It's true!

So, note that the 3 dots `...` are code block indicators in the Python terminal, that means they indicate that a command started above has not yet been finished. This way, we need to insert a blank line for Python to realize that we have finished that command and it can then execute it.

I think this is a good time to finish this first part of the tutorial :D

Don't forget to **comment** below with your opinion and questions!

See you in the next post!