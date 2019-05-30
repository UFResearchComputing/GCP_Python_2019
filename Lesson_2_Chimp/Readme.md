
# Lesson 2: Chimp Boxing Match

Gator Computing Program 2019.

Note that paths to images and other assets are formatted with Windows backslashes as these will be used in a classroom with Windows computers. If you are using online or on MacOS or Linux computers, you will likely need to update paths to have forward slashes.

Matt Gitzendanner

## Introduction

This tutorial is adapted from [this PyGame tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html). I was not able to find the original images or sounds used, so I grabbed some and adjusted the game screen a bit to fit.

Start by running the chimp.py program.

Open the Anaconda Prompt and change directories to the Lesson_2_Chimp directory. <img src="..\assets\notebook_images\Anaconda_Prompt_Launch.png" width=200 align="right">

In your Anaconda Prompt, change to your USB drive with the cloned repository and run the chimp.py program:

Type: `e:` (Or the drive letter of the drive with the repository.)

Type: `cd GCP_Python_2019/Lesson_2_Chimp`

Type: `python chimp.py`

Play the game a bit. You can use your mouse to move around. Click to hit the chimp. This is the starts of a fairly complex game and the code for it is relatively simple!

**Note**: The computers in the lab do not have speakers, you will need to plug in headphones to hear the sounds.

When you are done, either close the window or hit Escape to end the game.

Let's go through the script bit by bit.

## Imports

Like in the bouncy.py script from [Lesson 1](../Lesson_1_BouncyBall/bouncy.py) we need to import various Python modules. In the chimp.py script, we see a few ways of importing modules:

```python
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
```

 It is important to know that **how you import a module changes how you use its functions**. The next sections will look at some of the common ways of importing modules.

### `import module`

By writing `import os`, all of the functions of the "os" module are available, and are accessed using os.*function()*, for example: `os.path.join(os.pardir, "assets")`. That tells Python to look in the `os` module for the `path` function and within that, `join`.

### `import module as md`

For os, things are easy, but some modules have longer names, so we use the `import as` syntax, where we can rename the module with a shorter name. For example, many tutorials will use `import pygame as pg` since it is easier to type "`pg.display.flip()`" than "`pygame.display.flip()`"--coders are lazy! :stuck_out_tongue:

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

### Side note on `from pygame.locals import *`

In general, it is a bad idea to use things like `from pygame.locals import *`. Coders sometimes use this as another way of being laze. They can do something like `from pygame import *` and now instead of having to type `pygame.display.flip()`, they can just type `display.flip()`. But as with most things, being lazy has down sides. For example, it is no longer clear that the `display` function comes from pygame. Also if another module has a `display` function, we start getting really confusing code! So typically, we strongly discourage using the `from *module* import *` construct.

It turns out that pygame.locals is a set of environment variables, so probably OK in this case as that is how it is intended to be used, but this is a really special exception to the rule.

[Continue in part 2](Chimp_part_2.md)