Title: Python 101 - Parte 6 - Estruturas de Repetição - For
Date: 2022-08-09 12:06
Slug: python-101-parte-6
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hi!

One more post here teaching you Python and today we will talk about `for`.

In case you haven't seen the previous tutorials, we already have:

* [Introduction to Python]({filename}/Tutpriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutpriais/en/python101.2.md)
* [Conditional Structures in Python - 1]({filename}/Tutpriais/en/python101.3.md)
* [Conditional Structures in Python - 2]({filename}/Tutpriais/en/python101.4.md)
* [Repeat Structures - while]({filename}/Tutpriais/en/python101.5.md)


Let's start with a simple example:

    #!python
    l = [1, 2, 3, 4, 5]
    for i in l:
        print(i)

Here, initially, we start with something we haven't seen yet: __lists__.

We start by creating `l` as a list that contains a sequence of numbers.

So this list is used inside the `for`.

_In other languages, we determine the initial value of the counter variable, its limit and the iteration step. In python this does not happen. Here, for only iterates over sequences. This has several advantages, such as iterating over strings, or lists of different elements._

_It will be shown later because this for is not at a disadvantage compared to the for of other languages._

Then, at each iteration, the iteration variable, in this case `i`, receives the element of a position in the list.

Thus, this snippet above prints on the screen all the values ​​contained in the list `l`.

Now let's see this code snippet:

    #!python
    d = ['rice', 'beans', 'meat', 'potato']
    for i in d:
        print('I'm cooking ', i)

This example demonstrates the use of `for` with lists that contain *strings*, showing that you can use lists with any object in a `for`.

In `for` we can also use `break` and `continue`. Thus, we can further control the behavior of the loop. Also, there is a feature in Python's `for` that makes it very powerful: we can use an `else` at the end of the `for` as in the following example:

    #!python
    for i in ['a', 'b', 'c', 'd', 'e', ​​'f', 'g']:
        if i == 'h':
            break
        print(i)
    else:
        print('"h" is not in the list but I print anyway')


Using `else` at the end, we can control what will be executed at the end of a complete `for` execution and what will be executed if the loop is broken by a `break`. When the loop is completely traversed without a break, execution proceeds into `else`!

In this example, the output will look something like this:

    a
    b
    c
    d
    e
    f
    g
    "h" is not in the list but I print it anyway

This is very important, as it avoids having to do complicated tests to detect when a `for` is broken by a `break` that will be called under complex conditions.

Finally, many may be wondering: "How can this `for` be so powerful if we have to define the lists manually?"

The fact is that we don't have to do it manually if it's a list of numbers (just like we don't need to in other languages).

There is a Python function, range, which returns a _generator_ (object that can be iterated over like a list, but generates the values ​​at runtime) of numbers in the specified range. See the example:

    #!python
    for i in range(50):
        if i%2 == 0:
            print(i, 'is even')
        else:
            print(i, 'is odd')

When we do range(50), we will have a _generator_ that will work as a list of integers from 0 to 49. (try it in the shell).

Well folks! That's it for today!

Now it's not long before we start effective programming in Python!

In the next posts, native Python data types!

Be sure to post questions and opinions in the comments below!

See you in the next post!