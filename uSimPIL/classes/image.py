from PIL import Image as PILImage, ImageDraw as PILImageDraw
from typing import Union, Tuple, List, Dict, Any

from ..operations import *

def open(path: str):
    return Image(image=path)

def new(size: Tuple[int, int], color: Tuple[int, int, int, int] = (255, 255, 255, 255)):
    """Create a new image"""
    return Image(PILImage.new("RGBA", size, color))

def _convert(image: Union[str, "Image", PILImage.Image]):
    if isinstance(image, str):
        image = PILImage.open(image)
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        return image
    elif isinstance(image, PILImage.Image):
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        return image
    elif isinstance(image, Image):
        return image.image
    else:
        raise TypeError(f'"{type(image)}" is not a valid image type. Must be a string, PIL.Image or SimPIL.Image')

def merge(image: "Image", item: Union["Circle", "Corners"]):
    return Image(image, image.operations + item.operations)


class OperationsSystem:
    def __init__(self, operations: List[Operation] = []):
        self.operations: List[Operation] = operations

    def __repr__(self):
        return f"<OperationsSystem operations={self.operations}>"



class Image:
    def __init__(self, image: Union[str, "Image", PILImage.Image], operations: List[Operation] = []):
        self.image = _convert(image)
        self.operations = operations
        
        self.corners = Corners(operations, self)
        self.circle_crop = self.circle = Circle(self.operations)
    
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



class Corners(OperationsSystem):
    def __init__(self, operations: List[Operation] = [], image: "Image" = None):
        self.image = image
        super().__init__(operations)
    
    def roundall(self, radius: int):
        """
        Round the corners of an image

        Attributes
        ----------
        - radius (int) : The radius to use for the rounded corners (0 = square corners)
        """
        self.operations.append(RoundCornersOperation(radius, [True, True, True, True]))
        if self.image:
            return Image(self.image, self.operations)
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
        if self.image:
            return Image(self.image, self.operations)
        return Image(self.image, self.operations)

    def squareall(self):
        """
        Square all corners of an image
        """
        self.operations.append(RoundCornersOperation(0, [True, True, True, True]))
        if self.image:
            return Image(self.image, self.operations)
        return Image(self.image, self.operations)
    
    def square(self, corners: List[bool] = [True, True, True, True]):
        """
        Square specifics corners of an image

        Attributes
        ----------
         - corners (list[bool]) : A list of bools specifying which corners to square. The order is top-left, top-right, bottom-left, bottom-right.
        """
        self.operations.append(RoundCornersOperation(0, corners))
        if self.image:
            return Image(self.image, self.operations)
        return Image(self.image, self.operations)

    def circle_from_center(self, radius: int = 0):
        """
        Create a circle from the center of an image

        Attributes
        ----------
         - radius (int) : The radius of the circle
        """
        self.operations.append(CircleFromCenterOperation(radius))
        if self.image:
            return Image(self.image, self.operations)
        return Image(self.image, self.operations)


class Circle(OperationsSystem):
    def __init__(self, operations: List[Operation] = [], image: "Image" = None):
        self.image = image
        super().__init__(operations)
    
    def from_center(self, radius: int = 0):
        """
        Create a circle from the center of an image

        Attributes
        ----------
        - radius (int) : The radius of the circle
        """
        self.operations.append(CircleFromCenterOperation(radius))
        if self.image:
            return Image(self.image, self.operations)
        return self



    
    





# class MergeImages:
#     def __init__(self, images: List[Union[str, PILImage.Image, "Image"]], direction: str = "horizontal"):
#         self.images = []
#         for image in images:
#             self.images.append(_convert(image))
        
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


