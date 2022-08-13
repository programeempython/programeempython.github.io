Title: Python 101 - Parte 8 - Data Structures - Lists
Date: 2022-08-13 02:06
Slug: python-101-parte-8
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hi!

Today I'm going to talk about Lists in Python.

In case you haven't seen the previous tutorials, we already have:

* [Introduction to Python]({filename}/Tutoriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutoriais/en/python101.2.md)
* [Conditional Structures in Python - 1]({filename}/Tutoriais/en/python101.3.md)
* [Conditional Structures in Python - 2]({filename}/Tutoriais/en/python101.4.md)
* [Repetition Structures - while]({filename}/Tutoriais/en/python101.5.md)
* [Repetition Structures - for]({filename}/Tutoriais/en/python101.6.md)
* [Data Structures in Python - 1]({filename}/Tutoriais/en/python101.7.md)

Lists are ordered sets of data. In python, these sets can contain many mixed data types, since everything in Python is an object.

So, in addition to basic data types like integers, real numbers, and text, lists can contain any other language object.

Let's see how lists are created in python:

    #!python
    # Creating an empty list
    l = []

    #Creating a list with values
    l1 = [1, 2, 3, 'a', 'd', l]

    # Creating a list of letters from a string
    l2 = list("abracadabra")

In the first command, we create an empty list, which can be filled in the future. Next, we create a list, already assigning values ​​at the time of creation.

Note that when creating the list, integer values, letters and the list that was created empty previously are passed. Thus, we demonstrate that a list can receive any type of object, and that it can have objects of different types at the same time!

In the third list creation, we use `list()` to create a `list` object from a `string`. This is possible because both lists and strings are sequences.

But, Python lists are not static. We can insert and remove values ​​as we please at any time during program execution. Let's see:

    #!python
    # let's add values ​​to the list l created earlier
    # append(o) inserts an object o at the end of the list
    l.append(1) # the list will look like this [1]
    l.append(3) # the list will look like this [1, 3]
    
    # insert(i, o), insert object o at position i (first position is zero)
    l.insert(1, 2) # the list will look like this [1, 2, 3]
    l.insert(0, 5) # the list will look like this [5, 1, 2, 3]
    
    # remove(o) removes the first occurrence of the object o
    l.append(5) # the list will look like this [5, 1, 2, 3, 5]
    l.remove(5) # the list will look like this [1, 2, 3, 5]
    
    # pop(i) remove and return the object from position i
    # pop() removes and returns the last element of the list
    l.insert(3, 6) # the list will look like this [1, 2, 3, 6, 5]
    l.pop(3) # the list will look like this [1, 2, 3, 5] and return 6
    l.pop() # the list will look like this [1, 2, 3] and return 5
    
    #index(o) returns the index of the object o
    l.index(3) # returns 2
    l.append(3) # the list will look like this [1, 2, 3, 3]
    l.index(3) # keeps returning 2 as it is the first occurrence of 3
    
    # count(o) counts how many times the object o appears in the list
    l.count(1) # returns 1
    l.count(3) # returns 2
    l.pop() # the list will look like this [1, 2, 3] and returns 3
    
    # extend(L) extend list with list L
    l.extend([0, -1, -2]) # the list will look like this [1, 2, 3, 0, -1, -2]
    
    # sort() sorts the list items by itself
    l.sort() # the list will look like this [-2, -1, 0, 1, 2, 3]
    
    # reverse() reverses the elements of the list on itself
    l.reverse() # the list will look like this [3, 2, 1, 0, -1, -2]

Now it's time to exercise!

Open the terminal, and start playing with the lists! See how the commands work!

> A tip! The `help` command shows information about a command! try it after
> creating a list l, the command:
    >>> help(l.sort)

In the next post we will talk about an operation that has everything to do with lists: List Comprehension.

> A challenge!
>
> Who can imagine how to make a matrix in Python using what we saw today?
>
> Leave your answer in the comments!

Be sure to post questions and opinions in the comments below!

See you in the the next post!