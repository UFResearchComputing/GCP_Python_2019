# Part 5 of the chimp.py tutorial

[Continued from part 4](Chimp_part_4.md) | [Go to the start](Readme.md)

## The main loop of the program

Start an infinite loop, like we did with the bouncy.py example. Each loop is one frame of the game and is refreshed up to 60 times per second.

```python
#Main Loop
going = True
while going:
    clock.tick(60)
```

The `clock.tick(60)` limits the game to 60 frames per second at most.

```python
#Handle Input Events
for event in pygame.event.get():
    if event.type == QUIT:
        going = False
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        going = False
    elif event.type == MOUSEBUTTONDOWN:
        if fist.punch(chimp):
            punch_sound.play() #punch
            chimp.punched()
        else:
            whiff_sound.play() #miss
    elif event.type == MOUSEBUTTONUP:
        fist.unpunch()
```

Quoting from the [original tutorial](https://www.pygame.org/docs/tut/ChimpLineByLine.html):
>First we get all the available Events from pygame and loop through each of them. The first two tests see if the user has quit our game, or pressed the escape key. In these cases we just return from the main() function and the program cleanly ends.
>
>Next we just check to see if the mouse button was pressed or released. If the button was pressed, we ask the fist object if it has collided with the chimp. We play the appropriate sound effect, and if the monkey was hit, we tell him to start spinning (by calling his punched() method).

If the fist missed the chimp, call the `fist.unpunched()` method.

```python
allsprites.update()

#Draw Everything
screen.blit(background, (0, 0))
allsprites.draw(screen)
pygame.display.flip()
```

Call the `.update()` method on the `allsprites` RenderPlain to move the chimp and fist to their new positions for the new frame.

Then blank out the screen to the background, draw the new `allsprites` object on the screen and then flip the screen to the new view.

## Done!
And that's it!

Now, for you to play a bit...Things to try:

* Change the background color (do you need to change the transparency??)
* Change the text
* Get new images for the chimp and fist
* Get new sounds for the punch and miss (they need to be .wav files)
* Add up/down movement to the chimp
* Make the chimp movement change direction more often
* Keep track of score and print display how many times the chimp has been hit.
* Set a time limit and end the game after that time. If the user hits the chimp 10 times in the time limit they win, if not, they lose!