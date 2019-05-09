
# Lesson 2: Chimp Boxing Match

Gator Computing Program 2019

Matt Gitzendanner

## Introduction

This tutorial is adapted from [this PyGame tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html). I was not able to find the original images used, so I grabbed some and adjusted the game board a bit to fit.

Start by running the chimp.py program in your Anaconda Prompt type: `python chimp.py`

Play the game a bit. You can use your mouse to move around. Click to hit the chimp. This is the starts of a fairly complex game and the code for it is relatively simple!

When you are done, either close the window or hit escape to end the game.

Let's go through the script bit by bit.

## Imports

Like in the bouncy.py script from [Lesson 1](../Lesson_1_BouncyBall/bouncy.py) we need to import various python modules. In the chimp.py script, we see a few ways of importing modules:

```python
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
```
**Note:** in general, it is a bad idea to use things like `from pygame.locals import *`. I wouldn't recommend doing this, but that's how the example was written, so we'll stick with it. this imports everything ("*" is a wildcard, meaning "everything" or "all") and can cause problems with conflicts and other odd behavior.

It turns out that pygame.locals is a set of environment variables, so probably OK in this case, but in general, try to avoid the `from module import *` syntax. 

We've seen a few ways to import things. It is important to know that **how you import a module changes how you use its functions**. The next sections will look at some of the common ways of importing modules.

### `import module`

For example with `import os`, all of the functions of the "os" module are available, and are accessed using os.*function()*, for example: `os.path.join(os.pardir, "assets")`. That tells Python to look in the `os` module for the `path` function and within that, `join`.

### `import module as md`

For os, things are easy, but some module have longer names, so we us the `import as` syntax, where we can rename the module with a shorter name. For example many tutorials will use `import pygame as pg` since it's easier to type "`pg.display.flip()`" than "`pygame.display.flip()`"--coders are lazy! :stuck_out_tongue:

### `from module import function`

Another common syntax imports only certain functions (or sub-functions) of a module. Some modules are large and importing the whole thing is unnecessary if you only need one or two functions. It can also make using the function easier since that function is accessed directly by name rather than prefacing with the module name.

For example, here we are using `from pygame.compat import geterror`. Within pygame, there is a `compat` function and within that a `geterror` function. That is the only thing imported with this line. Line 30 shows how this is used:
```python
    raise SystemExit(str(geterror()))
 ```

 Since we imported all of pygame on the first line, we could write this line as
```python
    raise SystemExit(str(pygame.compat.geterror()))
```
but, the first is a lot easier. By using the `from module import function` syntax, `geterror` is accessible directly by name.  

[Continue in part 2](Chimp_part_2.md)