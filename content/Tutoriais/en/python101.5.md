Title: Python 101 - Part 5 - Repetition Structures - While
Date: 2022-08-07 22:11
Slug: python-101-parte-5
Category: Tutoriais
Tags: Tutorial, Python 101
Lang: en
Translation: true

Hi!

Let's keep talking about Basic Programming in Python! In case you haven't seen the previous tutorials, we already have:

* [Introduction to Python]({filename}/Tutoriais/en/python101.md)
* [Python Code Blocks]({filename}/Tutoriais/en/python101.2.md)
* [Conditional Structures in Python - 1]({filename}/Tutoriais/en/python101.3.md)
* [Conditional Structures in Python - 2]({filename}/Tutoriais/en/python101.4.md)

Today we are going to talk about one of the most important structures: the `while`.

The `while` is a statement that tells a block of code to be executed while a condition is satisfied. Thus, it allows execution loops to be created, as we have in games and applications with graphical interfaces.

`while` is a very useful statement, but it can be dangerous, because if we don't handle the stopping criterion correctly, the loop may never end, and the program doesn't do what it should.

Let's see an example of how `while` works in Python:

    #!python
    x = 100
    while x > 0:
        print("x > 0")
        x = x - 1

In this code, the message `x > 0` will be displayed until x is equal to zero. When the value of `x` goes to `0`, the check `x>0` will return false, the program exits the loop.

Now let's look at this code snippet:

    #!python
    i = 0
    while True:
        print("I will never stop!")
        i = i + 1
        if i > 100:
            break

Here we have a loop that would run forever (`while True:`). However, inside it, we do a check, and when the `i` variable is storing a value greater than `100`, the `break` command will be executed. The `break` command literally breaks the loop, so at that instant, the program exits the loop.

If just below this code we did a `print(i)`, the value displayed would be `100`.

So, along with the `while` command, we have now seen the `break` command which can be very useful for breaking loops outside the standard comparison.

Now let's look at the following snippet:

    #!python
    i=0
    while i < 100:
        i = i + 1
        if i % 2 == 0:
            continues
        print(i)

Initially, `i` is assigned the value `0`, and is compared to `100`. As `0` is less than `100`, the loop starts. Soon after, after incrementing the value of `i`, we have a comparison: if `1%2 == 0:`. here we check if `i` is a multiple of `2`. If `i` is a multiple of two, there is a `continue` command. `continue` causes this iteration of the loop to end and the program moves on to the next iteration. This way, the program ignores everything after `continue`.

In case `i` is not a multiple of `2`, the program does not execute `continue`, and prints the value of `i` on the screen.

If a `continue` were outside the `if`, the program would always execute this `continue`, and the one after it would never be executed. Thus, `continue` controls the execution of the loop without breaking it.

That's it for now.

Our next post will talk about the for statement.

Be sure to post questions and opinions in the comments below!

See you in the next post!