# uSimPIL
A ultra simplified version of Pillow


At the moment you can only modify the angles (rounded or squared) of an image (see examples/Round corners/example.py)

Example :
```py
import uSimPIL


img = uSimPIL.open("before.png")

img.corners.roundall(50)

img.create() # Used to apply modifications (will be of real use in the future)
img.save("after.png")
img.view()
```

## How it works
If you are interested in how it works but don't understand, basically I have the basic classes for image editing (e.g. modifying corners, borders, etc.) in /classes/image.py ; these classes (and functions) generate specific `Operations` (found in /operations.py) which will use functions from /utils/*
