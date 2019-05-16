# Part 4 of the chimp.py tutorial

[Continued from part 3](Chimp_part_3.md) | [Go to the start](Readme.md)

## The `main()` function

As you might expect, the main function takes care of the main part of the program. But there's a little more to this, so I wanted to point you to the last lines of the program now:

```python
 if __name__ == '__main__':
    main()
```

This is Python's way of allowing you to determine if someone ran your program or if they imported it into another program. We may decide to make a new game and in making that, we may realize that we want to load images and sounds and have a fist that punches, but maybe this time we want to turn this into a two player boxing match. While it would probably be easier in this little example to adapt the code for my new game, we *could* do `import chimp` or `from chimp import load_image, load_sound`, etc.

By using the `if __name__ == '__main__':` line, doing this would not start a chimp game, but only import the functions. If we just put the part of the code in the `main()` function after defining all the other functions and classes, once we import chimp, the chimp game would start, not what we want in that case.

How this works is if the program is run from the command line, the variable `__name__` has the value of `__main__`. Again, the underscores are there to indicate these should not be messed with directly, let Python manage their values.

## The parts of the `main()` function

```python
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 450))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)
```

`pygame.init()` makes sure everything is initialized correctly, then we set a screen dimension of 800 (wide) by 450 (tall) pixels, set a window caption and turn off the mouse cursor when in the window so that the fist is moving, not the cursor.

```python
#Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
```

Again quoting from the [original tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html):
>This creates a new surface for us that is the same size as the display window. Note the extra call to convert() after creating the Surface. The convert with no arguments will make sure our background is the same format as the display window, which will give us the fastest results.
>
>We also fill the entire background with a solid whitish color. Fill takes an RGB triplet as the color argument.

```python
#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)
```

Quoting the [original tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html) with a few minor modifications:
>As you see, there are a couple steps to getting this done. First we must create the font object and render it into a new surface. We then find the center of that new surface and **blit** (paste) it onto the background.
>
>The font is created with the font module's Font() constructor. Usually you will pass the name of a TrueType font file to this function, but we can also pass `None`, which will use a default font. The Font constructor also needs to know the size of font we want to create (36).
>
>We then render that font into a new surface. The render function creates a new surface that is the appropriate size for our text. In this case we are also telling render to create antialiased text (for a nice smooth look) (the "1") and to use a dark grey color `(10, 10, 10)`.
>
>Next we need to find the centered position of the text on our display. We create a "Rect" object from the text dimensions, which allows us to easily assign it to the screen center.
>
>Finally we blit (blit is like a copy or paste) the text onto the background image.

```python
#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
```
>We still have a black window on the screen. Lets show our background while we wait for the other resources to load.
>
>This will blit our entire background onto the display window. The blit is self explanatory, but what about this flip routine?
>
>In pygame, **changes to the display surface are not immediately visible**. Normally, a display must be updated in areas that have changed for them to be visible to the user. With double buffered displays the display must be swapped (or flipped) for the changes to become visible. In this case the flip() function works nicely because it simply handles the entire window area and handles both single- and double-buffered surfaces.

This is a bit unclear, but [this stackoverflow post](https://stackoverflow.com/questions/29135147/what-do-hwsurface-and-doublebuf-do) explains a bit more about double-buffered surfaces:
>Double-buffering, as the description for the tag mentions, is using a separate block of memory to apply all the draw routines and then copying that block (buffer) to video memory as a single operation. Failure to do this can lead to graphical artifacts. A simple example could be flickering of the scene caused by part of background being drawn right before the video refreshes and then other parts afterwards (so they aren't shown until the next refresh).

The post continues with more info, but that's the main bit to understand for our purposes.

```python
#Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound('Woosh-Mark_DiAngelo-4778593.wav')
    punch_sound = load_sound('Realistic_Punch-Mark_DiAngelo-1609462330.wav')
    chimp = Chimp()
    fist = Fist()
    allsprites = pygame.sprite.RenderPlain((fist, chimp))
```

Now we can finally get our game objects ready! The clock is used to control the game frame refresh rate. Then we load the sounds and images.

The last line, `allsprites = pygame.sprite.RenderPlain((fist, chimp))` creates a Sprites group called a RenderPlain which can draw our sprites (the fist and chimp) onto the screen.

[Continue to part 5](Chimp_part_5.md)