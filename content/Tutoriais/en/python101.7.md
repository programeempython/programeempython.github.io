Title: Python 101 - Part 7 - Data Structures - 1
Date: 2022-08-11 00:29
Slug: python-101-parte-7
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hi!

Today we are going to look at a very important thing in Python: the native data structures.

In case you haven't seen the previous tutorials, we already have:

* [Introduction to Python]({filename}/Tutoriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutoriais/en/python101.2.md)
* [Conditional Structures in Python - 1]({filename}/Tutoriais/en/python101.3.md)
* [Conditional Structures in Python - 2]({filename}/Tutoriais/en/python101.4.md)
* [Repetition Structures - while]({filename}/Tutoriais/en/python101.5.md)
* [Repetition Structures - for]({filename}/Tutoriais/en/python101.6.md)

There are several native Python data types. Among them, the most important, as they are essential for any program, are the types:

* `int` - integers
* `float` - floating point, representing the real numbers, basically
* `string` - string, or basically, text

However, in Python, unlike other languages, these data types, like all other structures in the language, are objects, so the basic type of everything in python is `object`. There's a lot to discuss about data types, but for simplicity's sake we'll consider it that way.

Returning to native data structures, we will see that these are structured sets of objects that can contain elements of any other type.

The first and perhaps most widely used of these structures is the `list`. A `list` implements a list that can contain virtually any object, consisting of as many object types as needed (unlike some languages).

In this way, lists become a very powerful tool within Python. We will have a post later focused especially on lists and their methods.

To create a list, simply assign values ​​to it as follows:

    #!python
    l = [1, 2, 3, 4, 5]

Just like we did when we saw how `for` works.

Another very important and widely used data structure is the `tuple`. Tuples contain sets of values ​​just like lists, but they differ from them mainly in that tuples cannot be changed after they are created, and lists can.

Let's create a tuple:

    #!python
    t = (1, 2, 3, 4, 5)

Now let's look at one of Python's most powerful data structures, and one that has many possibilities for use. This structure is the `dict` (dictionary) that relates key and value pairs.

So we create a dictionary:

    #!python
    d = {'a': 1, 'b': 2,'c': 3, 'd': 4, 'e': 5}

Finally, the last native Python data structure we'll look at today is the set. The sets represent mathematical sets. Thus, they are sequences and an interesting feature is that they do not have repeated elements.

For example, when creating this set:

    #!python
    s = set([1, 1, 2, 3, 5, 7, 13, 17])

The set will be `[1, 2, 3, 5, 7, 13, 17]`, as `1` appeared twice in the original list, and in the set it appears only once.

In the next posts, we will see these data structures in more detail :D

Be sure to post questions and opinions in the comments below!

Until the next post!