Title: Python 101 - Segunda Parte
Date: 2022-07-29 12:06
Slug: python-101-parte-2
Category: Tutoriais
Tags: Tutorial, Python 101
Summary:
Lang: en
Translation: true

Hi!

Now that we have Python installed and we already know its interactive interface, let's learn a little about the most basic commands of the language!

Before we continue, if you haven't read the previous post, go here:

[Python 101 - Part One]({filename}/Tutorials/python101.md)

As seen, in the Python shell we have two cursors:

    >>>
    ...

When we make an if, conditional structure that will be explained in more detail in a next post, we have the following in the console:

    >>> x = 0
    >>> if x < 1:
    ...     print("x is less than 1")
    ...
    x is less than 1

Now the explanation =]

In the first line, we say that the variable _x_ contains the value _0_;
Next, we compare the value contained in _x_ with _1_. When we end a command with **:** the interpreter understands that this is a command that did not end at the end of that line, and that it is composed of more commands, so the secondary cursor `...` gets in the game.

So, many programmers used to other languages ​​must ask themselves where are the curly braces to determine the block.

In Python, blocks are determined by indentation.

The lines that are inside the _if_, ie what must be executed if the comparison is true must be indented.

It is generally a convention, in Python, to use 4 spaces for the indentation.

The `print("x is less than 1")` is the command that should be executed if the comparison `x < 1` is true. Thus, this line is indented, and the interpreter knows that it should only execute it if *x* is less than *1*.

When you press `ENTER` at the end of this line, the interpreter shows you the secondary cursor again, because an `if` can have several commands inside. As we will see later, the execution of an entire program can be inside an __if__.

Thus, only after a second `ENTER` does the interpreter execute the command and display the result.

So, let's recap:

* Blocks in Python are defined by indentation
* The indentation must follow a pattern, preferably in all programs
* It is convention to use 4 spaces for indentation
* In the interpreter, indented blocks are preceded by the secondary cursor `...`
* A block indicates a snippet of code that is inside another command

That's all for now!

In the next Python 101 post we take the hint, and talk about conditional structures in Python!

Be sure to leave your questions and opinions in the comments below!

See you in the next post!