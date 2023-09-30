from PIL import Image as PILImage, ImageDraw as PILImageDraw
from typing import Union, Tuple, List, Dict, Any

from ..operations import *

def open(path: str):
    return Image(image=path)


class Modifications:
    def __init__(self):
        self.operations = []

class Image:
    def __init__(self, image: Union[str, "Image", PILImage.Image], operations: List[Operation] = []):
        if isinstance(image, str):
            self.image = PILImage.open(image)
        elif isinstance(image, PILImage.Image):
            self.image = image
        elif isinstance(image, Image):
            self.image = image.image
        
        self.operations = operations
        self.corners = Corners(self)
        
        # self.borders = Borders(self)

    def __repr__(self):
        return f"<Image image={self.image} operations={self.operations}>"
        
    def view(self):
        self.image.show()
    
    def show(self):
        self.image.show()

    def save(self, output_path):
        self.image.save(output_path)
    
    def create(self):
        for operation in self.operations:
            # self.image.show() # DEBUG
            self.image = operation.execute(self.image)
    



class Corners:
    def __init__(self, image: "Image"):
        self.image = image
        
        self.operations: List[RoundCornersOperation] = image.operations
        
    def roundall(self, radius: int):
        """
        Round the corners of an image

        Attributes
        ----------
        - radius (int) : The radius to use for the rounded corners (0 = square corners)
        """
        self.operations.append(RoundCornersOperation(radius, [True, True, True, True]))
        return Image(self.image, self.operations)

    
    def round(self, radius: int, corners: List[bool] = [True, True, True, True]):
        """
        Round specifics corners of an image

        Attributes
        ----------
         - radius (int) : The radius to use for the rounded corners (0 = square corners)
         - corners (list[bool]) : A list of bools specifying which corners to round. The order is top-left, top-right, bottom-left, bottom-right.
        """
        self.operations.append(RoundCornersOperation(radius, corners))
        return Image(self.image, self.operations)
    
    def squareall(self):
        """
        Square all corners of an image
        """
        self.operations.append(SquareCornersOperation([True, True, True, True]))
        return Image(self.image, self.operations)
    
    def square(self, corners: List[bool] = [True, True, True, True]):
        """
        Square specifics corners of an image

        Attributes
        ----------
         - corners (list[bool]) : A list of bools specifying which corners to square. The order is top-left, top-right, bottom-left, bottom-right.
        """
        self.operations.append(SquareCornersOperation(corners))
        return Image(self.image, self.operations)


# class MergeImages:
#     def __init__(self, images: List[Union[str, PILImage.Image, "Image"]], direction: str = "horizontal"):
#         self.images = []
#         for image in images:
#             if isinstance(image, str):
#                 self.images.append(PILImage.open(image))
#             elif isinstance(image, PILImage.Image):
#                 self.images.append(image)
#             elif isinstance(image, Image):
#                 self.images.append(image.image)
        
#         self.direction = direction
    
#     def merge(self):
#         if self.direction == "horizontal":
#             width = 0
#             height = 0
#             for image in self.images:
#                 width += image.size[0]
#                 height = max(height, image.size[1])
            
#             new_image = PILImage.new("RGBA", (width, height))
#             x = 0
#             for image in self.images:
#                 new_image.paste(image, (x, 0))
#                 x += image.size[0]
            
#             return Image(new_image)
#         elif self.direction == "vertical":
#             width = 0
#             height = 0
#             for image in self.images:
#                 width = max(width, image.size[0])
#                 height += image.size[1]
            
#             new_image = PILImage.new("RGBA", (width, height))
#             y = 0
#             for image in self.images:
#                 new_image.paste(image, (0, y))
#                 y += image.size[1]
            
#             return Image(new_image)
#         else:
#             raise ValueError("Invalid direction. Must be 'horizontal' or 'vertical'")


