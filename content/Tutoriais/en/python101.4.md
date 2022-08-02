Title: Python 101 - Part 4 - Conditionals in Python, the Return
Date: 2022-08-02 22:06
Slug: python-101-parte-4
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Continuing the article series on Conditional Structures in Python, we will now look at some other ways to use the `if`/`else` instructions.

If you haven't seen the previous post, here's the introduction to [Conditionals in Python](({filename}/Tutorials/python101.3.md))

It is often not possible to solve a computational problem simply with an `if`/`else`. So we use multiple nested `if`/`else` sets (one inside the other)

```Python
path = 3
if path == 0:
    print("Go back to the starting position")
else:
    if path == 1:
        print("Go ahead")
    else:
        if path == 2:
            print("Lower your head")
        else:
            if path == 3:
                print("You fell in the hole")
            else:
                print("Invalid option")
```

But, you can see that if you have a very nested structure of conditions, your code will be very messy... imagine thirty `if`/`else` instructions nested like that? It gets crazy!

So, to solve this problem, we have the `if`/`elif`/`else` construct. The `elif` plays the role of the `else` sequences that contain an `if`. See how the code is much more readable and organized!

```Python
d = 4

if d > 0:
    print("d is positive")
elif d < 0:
    print("d is negative")
else:
    print("d is null")
```

You can have as many `elif` as needed between `if` and `else`. See this example:

```Python
option = 2
if option == 0:
    print "The value chosen was 0"
elif option == 1:
    print "The value chosen was 1"
elif option == 2:
    print "The value chosen was 2"
elif option == 3:
    print "The value chosen was 3"
else:
    print "The chosen value is not valid"
```

The code remains organized and readable, helping you to understand the code!

Probably, at this point, people who know C, C++, java or some other languages ​​must be asking themselves: But where's the switch?

Actually, python doesn't have a switch like we have in other languages, and its function is very well fulfilled by the 'if'/'elif'/'else' structures. These structures still have advantages over some switch implementations that for example only do integer and single character comparisons.

It is possible to simulate a switch very efficiently and elegantly in Python, but that will be left for a next post with more advanced content.

In the next topic, we'll talk about Repetition Structures!

Don't forget to send your questions and opinions in the comments below!

See you in the next post!