Title: Python 101 - Part 10 - Data Structures - Dictionaries
Date: 2022-08-30 00:06
Slug: python-101-parte-10
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hi!

Today we are going to talk about a data structure that is not present in all languages. This structure is called a dictionary.

Python dictionaries are data structures that contain key-value pairs.

They are similar to lists, considering that both are sequences of elements, but accessing each position in the list is done differently.

In case you haven't seen the other articles in the Python 101 series, here they are:

* [Introduction to Python]({filename}/Tutoriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutoriais/en/python101.2.md)
* [Conditional Structures in Python - 1]({filename}/Tutoriais/en/python101.3.md)
* [Conditional Structures in Python - 2]({filename}/Tutoriais/en/python101.4.md)
* [Repeat Structures - while]({filename}/Tutoriais/en/python101.5.md)
* [Repeat Structures - for]({filename}/Tutoriais/en/python101.6.md)
* [Python Data Structures - 1]({filename}/Tutoriais/en/python101.7.md)
* [Python Data Structures - Lists]({filename}/Tutoriais/en/python101.8.md)
* [Python Data Structures - Comprehentions List]({filename}/Tutoriais/en/python101.9.md)

So let's see how to work with Dictionaries in Python!

To get started, let's look at ways to define a dictionary.

First we define an empty dictionary:

    #!python
    dictionary = {}

This dictionary can receive values ​​in the future during the execution of the program.

Now, let's imagine what it would be like to build a dictionary that listed strings for the days of the week, such as 'mon' and 'ter' with numbers. Indispensable if you're going to make a calendar, don't you think?

    #!python
    weekdays = {'sun' : 0, 'mon' : 1, 'tue' : 2, 'wed' : 3,
        'thu' : 4, 'sex' : 5, 'sat' : 6}

When we create a dictionary, it will have this structure. Before the `:` we have the key of the key-value pair, and after that, the corresponding value.

But, what if we were to create a dictionary that related the letters N, E, S, W of the cardinal points with numbers?

I bet you already know the answer! But, there is another way, also very useful to generate dictionaries, and that can be very important for generating these dictionaries at runtime.

Using `dict()` we can turn tuple lists into dictionaries. Technically it should be a sequence of sequences, but we'll use a list of tuples to illustrate that.

> If you don't remember what a tuple is, check out our [Introduction to Data Structures post]({filename}/Tutoriais/en/python101.7.md)

Here's how `dict()` works:

    #!python
    cardinal points = dict([('N', 0), ('E', 1), ('S', 2), ('W', 3)])

Do you remember the [List Comprehension]({filename}/Tutoriais/en/python101.9.md) we saw in the last post?

Well, how about using it to build a dictionary that lists the integers from zero to ten and their respective squares?

    #!python
    squares = dict([x, x**2 for x in range(11)])

It's very simple to create a dictionary, isn't it?

But... just creating the dictionaries is useless, right?

Let's see how to access a value from its key. let's use the days of the week dictionary. Try the commands in the Python Shell!

    >>> weekdays['tue']
    two
    >>> weekdays['sat']
    6

Easy, isn't it?

Shall we insert some values ​​into this dictionary?

    >>> weekdays
    {'wed': 3, 'sun': 0, 'sat': 6, 'fri': 5, 'mon': 1, 'thu': 4, 'tue': 2}
    >>> weekdays['Sun'] = 0
    >>> weekdays['Mon'] = 1
    >>> weekdays['Tue'] = 2
    >>> weekdays['Wed'] = 3
    >>> weekdays['Thu'] = 4
    >>> weekdays['Fri'] = 5
    >>> weekdays['Sat'] = 6
    >>> weekdays
    {'wed': 3, 'sun': 0, 'sat': 6, 'Sun': 0, 'mon': 1, 'fri': 5, 'Mon': 1,
    'thu': 4, 'Wed': 3, 'Sat': 6, 'Thu': 4, 'tue': 2, 'Fri': 5, 'Tue': 2}

In a dictionary, the order in which the elements appear is not so important, as the values ​​are accessed mainly through their respective keys, not their positions. In addition, dictionaries do not keep the order of elements, so the element that appears first in one execution may not be the first in another, even if the insertion was done in the same way.

If you need to check if a key is already in the dictionary, just do the following

    >>> 'mon' in weekdays
    true
    >>> 'bla' in weekdays
    false

Well, let's say now that I no longer want the dictionary to have the capitalized version for Sunday.

    >>> del(weekdays['Sun])

It is also possible to know which keys have already been inserted:

    >>> weekdays.keys()
    ['Sat', 'Mon', 'Fri', 'Wed', 'Thu', 'Tue', 'Wed', 'Sun', 'Sat', 'Fri',
    'Mon', 'Thu', 'Tue']

And what values ​​are in the dictionary:
    >>> weekdays.values()
    [6, 1, 5, 3, 4, 2, 3, 0, 6, 5, 1, 4, 2]

One important thing to note is that keys and dictionary elements can be of virtually any type, with the exception of keys which have a constraint. Objects have to be immutable.

This means that the list `[1, 2, 3]` cannot be a dictionary key as we can change values ​​in the list in the middle of the execution. The tuple `(1, 2, 3)` that is immutable can be a dictionary key without any problems.

By now, you are familiar with Python Dictionaries, this data structure that has so many important applications.

Be sure to post questions and opinions in the comments below!

See you in the next post!
