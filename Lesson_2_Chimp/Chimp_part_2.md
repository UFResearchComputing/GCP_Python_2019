
# Part 2 of the chimp.py tutorial

[Continued from part 1](Readme.md) | [Go to the start](Readme.md)

## The `if not` statements

We looked at `if` statements in the bouncy.py exercise. These lines are an example of a shortened syntax for an `if` statement.

```python
if not pygame.font: print ('Warning, fonts disabled')
```

The `print` statement could be on the next line (indented) but in this example is on the same line. Again, just a bit shorter and more compact.

The purpose of these lines is to warn the user if the `pygame.font` or `pygame.mixer` functions weren't loaded correctly.

## Functions

The next couple of sections define some functions. Functions are a way of making code re-usable. Rather than having to copy/paste sections of code, once you realize you might want to do something more than once, like load an image or a sound in this case, write a function that can load *any* image or *any* sound. That way you can reuse what you have written and, as you make improvements and fix bugs, there is only one copy of the code to fix.

Let's look at an example of a simple function. Copy this into a Jupyter notebook cell and execute it.

```python
def add_two(a,b):
    sum=a+b
    return sum
```

Nothing happened right? *That's not quite true*...you didn't get any output, but you did define a function!

In the next cell, type: `type(add_two)`

Jupyter should tell you that `add_two` is a function.

To call this function, we can type: `add_two(2,3)`

And we should get 5 as the answer.

Python functions start with the word `def` followed by the name of the function and then parentheses. Within the parentheses, are the names of variables to store any input passed into the function (or empty parentheses if no input is needed). The end of the line has a ":".

The rest of the function is indented. If desired, a function can return one or more values--the sum in this case. Not all functions return something, some functions return multiple values.

Play with this a bit and make sure you understand how this works.

* What happens if you pass strings (characters) into the `add_two` function?
* What happens if you don't pass anything? Or 3 numbers?
* Assign the result to a variable.

### The `load_image` function

OK, now we can tackle the `load_image` function:

```python
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
```

This function takes as input the name of an image file and the colorkey, which has the default value of None. This means that if we pass two values in the call to `load_image()`, the second value will be used for colorkey, if we only pass one, then the default "None" is used. We will come back to this in a bit.

Think about your `add_two` function. How could you modify this so that a user could pass in 2 or 3 numbers to be added together? Make that change and test it.

Within the `load_image` function, we use `os.path.join()` to join the data_dir (defined above) and the name of the image file we want to load (stored in the `name` variable within the function). 

A more general approach might be to have the function take the full path or also take the data_dir, but for this program, this will work. But what would happen if my images were in different directories?

#### `try:` and `except:`

The next part of the function uses the `try:` and `except:` construct to **try** to load the image, but if something goes wrong, like the image is not there or cannot be read, do not just crash the program (which is what would happen if we just loaded the image and got an error), but do something else. The `except:` part of this only gets run if there is an error in loading the image. In this case, if we get an error, print a message and tell the user what the error was.

It is really good practice to use `try:` and `except:` whenever there is a chance that you will get an error. This gives you the chance to handle that error more gracefully than just crashing the program. Or maybe you will do something different if there is an error, like use a different file or download it from the internet and then load it.

#### The `image` Surface object

The pygame function `image.load()` opens the image file and loads it into a pygame [Surface object](https://www.pygame.org/docs/ref/surface.html). Every image in a game is represented by a Surface and there are many pre-built methods that can be used to manipulate these.

The first manipulation, `image=image.convert()`, matches the imported image to the display which makes it faster to draw the image. This is always a good first step when starting to work with an image Surface.

#### Colorkey

Colorkey allows you to set a color in the image that is transparent.

```python
if colorkey is not None:
    if colorkey is -1:
        colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
```

If the call to the `load_image()` function passed in a second value, then the `colorkey` variable will have a value other than None (e.g. it will be `not None`).

One option is to use the color of the top left pixel of the image to set the transparent color. You can pass "-1" as the second parameter, which makes the second `if` true and calls `image.get_at(0,0)` to get the color of the (0,0) pixel (top,left).

Otherwise, you can pass in a color value to use for the transparent color.

`image.set_colorkey` as you might expect, sets the colorkey value. The `RLEACCEL` helps with speed of changing the image during the game.

#### Return values

The `load_image` function returns two things. One is the `image` object and the second is the size of the image, obtained with the `.get_rect()` method. When we get to that point further down, we will see that a call to `load_image` has two variables to assign the results to since we are getting two things back:

```python
self.image, self.rect = load_image('chimp.jpeg', -1)
```

### The `load_sound` function

```python
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound
```

This is fairly similar to what we did for the image.

We will cover the `class` bit in the next section, but for now, just think of this as handling the case where the `pygame.mixer` module did not load properly. This just creates a silent "sound" to have something to work with.

[Continue to part 3](Chimp_part_3.md)