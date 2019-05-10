# Part 3 of the chimp.py tutorial

[Continued from part 2](Chimp_part_2.md) | [Go to the start](Chimp.md)


## Classes

To understand classes, we need to learn a little about what is referred to as "Object Oriented Programming" or OOP. OOP makes it easier to code programs by allowing to programmer to partition the code. For more information on OOP in Python, I highly recommend the [OOP chapter](https://www.py4e.com/html3/14-objects) in [Python For Everybody](https://www.py4e.com/).

A class is used to create the definition of some concept in the program and then create individual objects or instances of that class. By making classes, concepts within a program can be packaged and worked on in isolation of the rest of the program. 

Think about a class to work with a table. ![Table image](../assets/notebook_images/table.jpg). This class would have ways of describing the table, how many legs it has, what material it is made out of, how many people can sit at it, etc. In our program, we could define the class, and then create an individual object for each table we need to keep track of.

In addition to holding information (data) about each object, the class can have functions to work on the object. These are called **methods**. For example, there may be a method to set the table. Or a method to arrange the chairs (and the chairs would be objects defined by a different class, the chair class).

Classes and the objects they create sound kind of abstract, but they are used all the time without us thinking about it.

Let's look at a string. Paste this into a Jupyter notebook cell and run it.

```python
mascot="Gators"
print("Go", mascot, "!")
type(mascot)
```

You should see "Go Gators !" and that `mascot` is of type str (short for string).

Now try this: `print("Go", mascot.upper(),"!")`

`mascot` is an *object* made with the string class. One of the *methods* of the sting class is to make the string uppercase. Just as one of the methods of our table class might have been to set the table.

To see what methods are available for any object, you can use the `dir()` function. Type: `dir(mascot)` to see the string methods.


## Class inheritance

One cool thing is that we don't need to start from scratch every time we write a class. One class can inherit, or include the methods, from another class.

Rather than get into the details of inheritance here, take a look at the example in the [Python for Everybody](https://www.py4e.com/html3/14-objects) book or this example from Digital Ocean on [Understanding Class Inheritance in Python 3](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3). 

### The `Fist` class

Our program defines two classes, one for the fist and one for the chimp. Each class needs to have different methods--the fist needs to move with the mouse, punch, etc. while the chimp moves on its own, spins when hit, etc. So it makes sense that these are different classes.

```python
class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('fist.png', -1)
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        "returns true if the fist collides with the target"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        "called to pull the fist back"
        self.punching = 0
```

The `Fist` class inherits all the methods of the [`pygame.sprite.Sprite` class](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) and adds four methods, \_\_init\_\_, update, punch, and unpunch.

The `pygame.sprite.Sprite` class has methods for things like add, remove, kill, alive. While it does have basic \_\_init\_\_ and update methods, coders are instructed to **overwrite**, or make their own methods in their **child** classes (a child is the class the inherits the parent class--our First class is a child of the parent Sprite class).

#### The `__init__` method

The \_\_init\_\_ method is what is called when an new object of the class is created, or *init*ialized. 
First, we call the Sprite \_\_init\_\_ method. In the next line, we call our `load_image` function to load the fist.png image and set the transparent color to the top left pixel color. **Notice** `load_image` returns two values, stored in `image` and `rect`--the `rect` is the size of the image. Lastly, we set the value of `punching` to 0.

Actually, you may have notices that the returned values are stored in `self.image` and `self.rect`. The `self` here refers to the name of the actual object we are working on. Remember that the class defines the properties and methods and is used to create an individual instance of that class, the object itself. Each object has it's own values of `image` and `rect` and it does this using `self.` ahead of those variable names.

#### The `update` method
The update method deals with moving the fist on the screen to follow the mouse.

`pos = pygame.mouse.get_pos()` gets the mouse position.

The next line gets the midtop point of the fist image. Details are a bit sketchy here in the pygame documentation...[this page](https://www.pygame.org/docs/ref/rect.html) says:

>The Rect object has several virtual attributes which can be used to move and align the Rect:
>
>```
>x,y
>top, left, bottom, right
>topleft, bottomleft, topright, bottomright
>midtop, midleft, midbottom, midright
>center, centerx, centery
>size, width, height
>w,h
>```

The last bit, moves the image 10 pixels over and 20 down when you click the mouse to punch.

#### The `punch` method
In addition to the fist object, this method needs to know what is being punched, the target, so that it can calculate if you hit or miss the target.

When the punch method is called, `punching` is probably 0, so the first thing to do is set it to 1.

Then we calculate the `hitbox`, or where the fist is when the mouse is clicked. The `rect.inflate` grows, or shrinks with negative numbers, the rect object. I think this is here to compensate for the movement of the fist when you click. Either way...a new method to know about...

The last line returns a True/False that comes from a call to the `.colliderect()` method on the new hitbox object passing in the target.rect--True if they overlap, false if not.

### The `Chimp` class

```python
class Chimp(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('chimp.jpeg', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0

    def update(self):
        "walk or spin, depending on the monkeys state"
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        "move the monkey across the screen, and turn at the ends"
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        "spin the monkey image"
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        "this will cause the monkey to start spinning"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image
```
Rather than go into the details of everything here, I'm going to quote the [original tutorial text](https://www.pygame.org/docs/tut/ChimpLineByLine.html) on this class:

>The chimp class is doing a little more work than the fist, but nothing more complex. This class will move the chimp back and forth across the screen. When the monkey is punched, he will spin around to exciting effect. This class is also derived from the base Sprite class, and is initialized the same as the fist. While initializing, the class also sets the attribute "area" to be the size of the display screen.
>
>The update function for the chimp simply looks at the current "dizzy" state, which is true when the monkey is spinning from a punch. It calls either the _spin or _walk method. These functions are prefixed with an underscore. This is just a standard python idiom which suggests these methods should only be used by the Chimp class. We could go so far as to give them a double underscore, which would tell python to really try to make them private methods, but we don't need such protection. :)
>
>The walk method creates a new position for the monkey by moving the current rect by a given offset. If this new position crosses outside the display area of the screen, it reverses the movement offset. It also mirrors the image using the pygame.transform.flip function. This is a crude effect that makes the monkey look like he's turning the direction he is moving.
>
>The spin method is called when the monkey is currently "dizzy". The dizzy attribute is used to store the current amount of rotation. When the monkey has rotated all the way around (360 degrees) it resets the monkey image back to the original, non-rotated version. Before calling the transform.rotate function, you'll see the code makes a local reference to the function simply named "rotate". There is no need to do that for this example, it is just done here to keep the following line's length a little shorter. Note that when calling the rotate function, we are always rotating from the original monkey image. When rotating, there is a slight loss of quality. Repeatedly rotating the same image and the quality would get worse each time. Also, when rotating an image, the size of the image will actually change. This is because the corners of the image will be rotated out, making the image bigger. We make sure the center of the new image matches the center of the old image, so it rotates without moving.
>
>The last method is punched() which tells the sprite to enter its dizzy state. This will cause the image to start spinning. It also makes a copy of the current image named "original".

[Contiune to part 4](Chimp_part_4.md)
