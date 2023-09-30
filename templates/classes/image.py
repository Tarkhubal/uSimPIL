from PIL import Image as PILImage, ImageDraw
from typing import overload, Union, Optional, List, Dict

from classes.text import Text

class Image:
    def __init__(self, image: str):
        """Load an image
        
        Attributes
        ----------
         - image (str) : path to the image
        """
        self.image = PILImage.open(image)
        self.corners = Corners(self)
        self.border = Borders(self)
        self.merge = Merge(self)
    
    @property
    def view(self):
        self.image.show()
    
    def save(self, path: str):
        """Save the image
        
        Attributes
        ----------
         - path (str) : path to save the image
        """
        self.image.save(path)
    

class Merge:
    def __init__(self, image: Image):
        self.img = image
        self.images = MergeImages(self.img)
    
    def from_simpil(self, obj: Union["Corners", "Text", "Borders"]):
        """Merge a SimPIL item (like text) with the image"""
    

class MergeImages:
    def __init__(self, image: Image):
        self.image = image
    
    def from_path(self, path: str, merge_method: int = 5):
        """
        merge_method (align) :
          1 = top
          2 = right
          3 = bottom
          4 = left
          5 = center
        """
        ...
    
    def from_simpil(self, image: "Image"):
        ...


class Corners:
    def __init__(self, image: Image):
        self.image = image

    def round(self, radius: int):
        image = Image.open(self.image.image)
        image = image.convert("RGBA")

        rounded = Image.new("RGBA", image.size)
        draw = ImageDraw.Draw(rounded)
        draw.rounded_rectangle([0, 0, *image.size], fill=(255, 255, 255, 255), radius=radius)

        result = Image.alpha_composite(rounded, image)
        result.show()
        
    
    def roundall(self, percent: int):
        """Round all corners of the image
        
        Attributes
        ----------
        percent (int) : % of rounding (0 = no round, 100 = circle image)
        """

    def square(self, corners):
        """Square corners of the image
        
        Attributes
        ----------
        corner (tuple[int]) : a tuple of all corners to round (0 = top left, 1 = top right...)
        
        Example :
        ```py
        Image.corners.square((0, 1, 3), 100)
        # Here, all corners except the bottom right will be squared
        ```
        """
     
    def squareall(self):
        """Square all corners of the image"""
        self.roundall(0)



class Borders:
    def __init__(self, image: Image):
        self.image = image
    
    def reset(self):
        ...
    
    def add(self, position: tuple[int], color, width: int):
        ...
    
    def addall(self, color, width: int):
        ...






    
    
    
