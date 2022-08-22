Title: Python 101 - Parte 9 - Data Structures - List Comprehention
Date: 2022-08-22 23:06
Slug: python-101-parte-9
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hello!

As promised, today we are going to continue the post talking about lists in Python, as this is a very extensive subject.

Today's topic is List Comprehension.

List Comprehension is a Python feature that allows the creation of lists in a simple way, simply using an expression followed by a `for` that can contain another `for` and/or `if` within it.

Everything will become clearer as we move on to the examples.

So, let's get our hands dirty! Open the Python shell.

Remember that what must be typed will be preceded by `>>>` or `...`, as it will appear in the python shell.

If by any chance you don't understand what I'm talking about, it's advisable that you read the previous posts beforehand, which will keep you up to date with everything we've seen so far.

* [Introduction to Python]({filename}/Tutoriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutoriais/en/python101.2.md)
* [Conditional Frameworks in Python - 1]({filename}/Tutoriais/en/python101.3.md)
* [Conditional Frameworks in Python - 2]({filename}/Tutoriais/en/python101.4.md)
* [Repeat Structures - while]({filename}/Tutoriais/en/python101.5.md)
* [Repeat Structures - for]({filename}/Tutoriais/en/python101.6.md)
* [Python Data Structures - 1]({filename}/Tutoriais/en/python101.7.md)
* [Python Data Structures - Lists]({filename}/Tutoriais/en/python101.8.md)

Try to understand exactly what happens in each example. Come on!

    >>> l = [1, 2, 4]
    >>> [3 * x for x in l]
    [3, 6, 12]
    >>> [2 * x for x in l if x > 3]
    [12]
    >>> 5 * x for x in l if x < 0]
    []
    >>> [[x, 2*x] for x in l]
    [[1, 2], [2, 4], [4, 8]]
    >>> [(x, 2*x) for x in l]
    [(1, 2), (2, 4), (4, 8)]
    >>> l1 = [0, 1, 2]
    >>> l2 = [1, 2, 3]
    >>> [x * y for x in l1 for y in l2]
    [0, 0, 0, 1, 2, 3, 2, 4, 6]
    >>> [l1[i] * l2[i] for i in range(len(l1))]
    [0, 2, 6]

The instructions are always given in the same pattern:

    [<expression> for <variable> in <list> [if <condition>] [for...]]
    *** Structures between [] are optional. ***

Now we come to the point where we must answer last Python 101 post's challenge in order to proceed.

> "Who can imagine how to make an array in Python using what we saw today?"

The answer is: **Create lists of lists!**

So if we do:

    >>> m = [[1, 2, 3],[2, 3, 4]]

We will have the matrix m with 2 rows and 3 columns, containing in the first row the values ​​`1, 2, 3` and in the second the values ​​`2, 3, 4`.

So we can use `list comprehention` to create matrices as well. We call this feature Nested List Comprehention.

Let's look at the following example:

    >>> m = [
    ... [1, 2, 3],
    ... [4, 5, 6],
    ... [7, 8, 9],
    ... ]

Here, we create a 3x3 matrix with values ​​from 1 to 9.
Now, here's a way to exchange the rows with the columns of the matrix m:

    >>> [[line[i] for line in m] for i in [0, 1, 2]]
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

I think for today, this feature is well illustrated. Be sure to post questions and opinions in the comments below!

See you in the next post!