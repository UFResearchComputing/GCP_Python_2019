# Chimp Boxing Match

This tutorial is adapted from [this PyGame tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html). I wasn't able to find the original images used, so I grabbed some and adjusted to gameboard a bit to fit.

Start by running the chimp.py program in your terminal: `python3 chimp.py`

Play the game a bit. You can use your mouse to move around. Click to hit the chimp. This is the starts of a fairly complex game and the code for it is relatively simple!

When you are done, either close the window or hit escape to end the game.

Let's go through the script bit by bit.

## Imports
Like in the bouncy.py script from [Lesson 1](../Lesson_1_BouncyBall/bouncy.py) we need to import various python modules.

```python
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
```
**Note:** in general, it is a bad idea to use things like `from pygame.locals import *`. I wouldn't recommend doing this, but that's how the example was written, so we'll stick with it. It imports everything ("*" is a wildcard, meaning everything or all). 

We've seen a few ways to import things and how you import a module changes how you use its functions.

### `import module`
For example with `import os`, all of the functions of the "os" module are available, but are accessed using os.*function()*, for example: `os.path.join(os.pardir, "assets")`. 

### `import module as md`
For os, things are easy, but some module have longer names, so we us the `import as` syntax, where we can rename things, usually with a shorter name. For example many tutorials will use `import pygame as pg` since it's easier to type "`pg.display.flip()`" than "`pygame.display.flip()`"--coders are lazy!

### `from module import function`
Another common syntax imports only certain functions (or sub-functions) of a module. Some modules are large and importing the whole thing is unnessessary if you only need one or two functions. It can also make using the function easier since that function is accessed directly by name rather than prefacing with the module name.

For example, here we are using `from pygame.compat import geterror`. Within pygame, there is a compat function and withing that a geterror function. That is the only thing imported with this line. Line 30 shows how this is used:
```python
    raise SystemExit(str(geterror()))
 ```

 Since we imported all of pygame on the first line, we could write this line as
```python
    raise SystemExit(str(pygame.compat.geterror()))
```
but, the first is a lot easier. By using the `from module import function` syntax, geterror is accessible by name.  

## The `if not` statements
