Title: Python 101 - part 3 - Python Conditional Structures
Date: 2022-08-01 23:06
Slug: python-101-parte-3-condicionais
Category: Tutoriais
Tags: Tutorial, Python 101, Condicionais
Lang: en
Translation: true

Hi!

Continuing our introductory Python series, let's talk a little about conditional structures.

If you haven't seen the previous post, see here to understand the [Python Code Blocks]({filename}/Tutorials/python101.md)

Conditional structures are essential in programming. Without them, programs would be boring, monotonous, and would never have been able to do what they do today.

__Without conditional structures there would be no video games!!!!__

So, let's see how Python implements its conditional structures.

Python's main conditional structure (and most used as well) is the `if`/`else` construct or its `if`/`elif`/`else` variation.

These constructions will guide us through the execution of a code snippet. If this, do that, if not, do that other thing...

Below is an example of using `if`/`else`:

    #!python
    x = 3
    if x % 2 == 0:
        print("x is even")
    if no:
        print("x is odd")


This code parses the value of the variable `x`. If `x % 2` (the remainder of dividing `x` by `2`) is equal to zero, then the number is even, otherwise it is odd. We will see more math functions in future posts.

When typing these commands in the terminal, it would look like this:

    >>> x = 3
    >>> if x % 2 == 0:
    ... print("x is even")
    ... if no:
    ... print("x is odd")
    ...
    x is odd

To recap what was said in the text about blocks of code in Python, when we have a block identified just below a command ending in :, a block that is directly related to this command.

In the example, we have the command `if x%2==0:` and just below the print `"x is even"` identified. This means that the code identified (`print("x is even")`) will only be executed if the remainder of the division `x` by `2` is zero.

If this result is non-zero, x is not even, and the interpreter encounters the command `else:`.

Below this command, `print which is identified as the case which is interpreted which should be executed in comparison within the `false if`).

We will not cherish the matter. For now we stop here, but hope that soon we will have a sequel for you!

Feel free to post questions and comments in the comments below!

Until the next post!