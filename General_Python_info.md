# Python Vocabulary Check and Recap

## **Documentation**

### [Python 3 documentation](https://docs.python.org/3/)

### Definition

The user-manual of how to begin using a programming language and what features it supports. Many popular languages support their own documentation, and more obscure languages may have documentation but the extent of what they cover maybe less.
While programming languages most commonly have documentation, packages also do as well.

With Python, the documentation on their main website has pages for:

1. Tutorial - getting started
2. Library Reference - what you can do
3. Language Reference - how you can do it
4. Python Setup / Installing - how to start doing what you want to do
5. HOW-TOs - other things you can do

For an extensive package like Pandas, the documentation can be found with a quick
[Google search](http://lmgtfy.com/?q=pandas+python+documentation) where you will ultimately end up at
[this](https://pandas.pydata.org/pandas-docs/stable/) similarly formatted page. There is an additional page [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html#overview) that details an overview of the package.

With Pandas, their documentation has larger categories like:

1. Installation
2. Getting Started
3. User Guide

that give some perspective into the power of Pandas and the [data structures](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html) that it provides.

And, depending on your final project, additional information on PyGame would definitely be nice to have! Due to the popularity of this extension, they have a full-blown website at [pygame.org](https://www.pygame.org) with documentation conveniently located at [pygame.org/docs](https://www.pygame.org/docs).

With Pygame, they provide sections for:

1. Documents
2. Tutorials
3. Additional reference

All of these sections provide links to more in-depth articles of how to implement certain features to your game, along with things you may be familiar with (the chimp, perhaps).

---

## **Packages**

### [Reference page](https://www.learnpython.org/en/Modules_and_Packages)

### [PyPi](https://pypi.org/)

Website for sharing many kinds of packages, with different uses. Most any of these packages can be installed with the 'pip install'

### Textbook Definition

In programming, a module is a piece of software that has a specific functionality. For example, when building a ping pong game, one module would be responsible for the game logic, and another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited separately. The most common are mathematics, statistics, and web request libraries.

### Simplified definition

A set of code that has been written already and can be linked to your code to provide functionality. We have previously used pygame, pandas, and matplotlib to provide easy ways to create otherwise complex operations.



### Implementation

Before anything is done with a package or module, the following is necessary:

1. That it is installed with  `pip install *package*`

2. `import *package*` is used to bring it into your program

Where `*package*` is replaced by the name of the package you have installed

Afterwards, your code may look like this snippet from our example:

    # Imports the sys and os packages (pre-installed)
    # Additionally imports pygame (needs to be installed)
    import sys, os
    import pygame


    # Utilizes the init() method from the pygame package by calling
    # the package name, a period, the method/function name

    # Additional functions can be found in documentation
    pygame.init()

---

## **More resources**

While we have provided examples in class and the information above for documentation and packages, we've only scratched the surface in terms of what Python can do! Below are a few websites that can help to bolster aspects of Python you want to learn about, practice, or challenge yourself with in the future.

### [HackerRank](https://www.hackerrank.com/domains/python)

HackerRank, more utilized by college students or potential job-seekers, provides numerous challenges to test your knowledge of Python (and other programming languages). They even offer a 30-days of coding where you are progressively challenged with increasingly difficult problems that help to reinforce your familiarity and knwoledge with programming. Some parts of the website can be paid but a majority of it can be accessed for free.

### [w3schools](https://www.w3schools.com/python/default.asp)

The classic online tutorial website w3schools features many tutorials for web development, which includes Python. The main appeal of w3schools is its ability to cover many aspects of a language by offering examples with testable code, challenging the user with exercises, and providing additional references to the topics discussed. This website does a good job in conveying the basics of Python, while also allowing you to become familar with other programming languages as well.

### [No Starch Press](https://nostarch.com/catalog/python)

A personal favorite of mine is No Starch Press, an online book publisher that provides "the finest in geek entertainment" yeah...
They have numerous programming languages covered with varying, often beginning, skill levels and while the price for them can be upwards of \$30 (birthday presents, anyone?) you can also find them online through libraries, e-book retail websites, Amazon, and sometimes on sale through the Humble Bundle quite often. These well-written, educational books give many examples on the reasoning behind why things are done a particular way and how you can utilize them!

### Other resources

Outside of these listed resources, there are many, many websites to help you with different topics or aspects of programming, along with books that provide additional clarification. While these are mostly Python/programming focused, the amount of tutorials and books available for **anything** is enormous, and are often available for free to anybody.
