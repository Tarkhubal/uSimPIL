# Getting Started

Welcome to you, young adventurer in the world of uSimPIL!

In this first chapter of your new story, you will learn the basic workings of the library.

To get started, here's a simple little example:

```py
import uSimPIL

img = uSimPIL.open("before.png")
img.corners.roundall(radius=50)

img.create() # Used to apply modifications (will be of real use in the future)
img.save("after.png")
img.view()
```

It's quite simple to understand, isn't it? (If you don't agree, open an issue T-T)

The goal of this little program is simply to round the corners of the image `before.png` (yes that's all)

## Analysis

Okay, now that we have that, let's analyze this program in a little more detail:

Here we start with this line:

```py
img = uSimPIL.open("before.png")
```

This little line allows you to open the image called "before.png" and load it into uSimPIL (easy in real life)

Then comes this line:

```py
img.corners.roundall(radius=50)
```

Here, we could break it down into several parts: `img` corresponds to our loaded image, `corners` asks the program to act on its angles and `roundall` allows us to round all the angles of the image. The small `radius=50` allows you to round the corners by 50 pixels

Simple, right? 👀

If we continue, we will notice this line:

```py
img.create()
```

As indicated in the comments (at the very top), this line allows you to apply the modifications to the image. Indeed, uSimPIL does not apply the modifications directly, it stores the modification steps in the given order and applies them at the time of this line, this allows you to do a kind of "Ctrl+Z" if necessary (we will see that in a next chapter don't worry)

```py
img.save("after.png")
img.view()
```

Then, the last two lines do not vary much from Pillow, they allow, respectively, to save then display the image (an equivalent of an Image.show() on Pillow)
