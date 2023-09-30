# SimPIL
A simplified version of Pillow


At the moment you can only modify the angles (rounded or squared) of an image (see examples/Round corners/example.py)

Example :
```py
import SimPIL


if __name__ == "__main__":
    img = SimPIL.open("before.png")
    
    img.corners.roundall(50)
    
    img.create() # Used to apply modifications (will be of real use in the future)
    img.save("after.png")
    img.view()
```
