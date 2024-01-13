from PIL import Image as PILImage
from typing import List, Union, Tuple

from .utils import *

class Operation:
    def __init__(self):
        pass
    
    def execute(self, image: PILImage.Image):
        pass
    
    def __repr__(self):
        return f"<Operation>"


class OperationsSystem:
    def __init__(self, operations: List[Operation] = []):
        self.operations: List[Operation] = operations

    def __repr__(self):
        return f"<OperationsSystem operations={self.operations}>"


class RoundCornersOperation(Operation):
    def __init__(self, radius: int, corners: List[bool]):
        self.radius = radius
        self.corners = corners
    
    def __repr__(self):
        return f"<RoundCornersOperation radius={self.radius} corners={self.corners}>"
    
    def execute(self, image: PILImage.Image):
        # print("Executing corners operation")
        return round_corners(image, self.radius, self.corners)

class CircleFromCenterOperation(Operation):
    def __init__(self, radius: int):
        self.radius = radius
    
    def __repr__(self):
        return f"<CircleFromCenterOperation radius={self.radius}>"
    
    def execute(self, image: PILImage.Image):
        # print("Executing circle from center operation")
        return circle_from_center(image, self.radius)

class TextOperation(Operation):
    def __init__(self, text: str, position: Union[Tuple[int, int], Tuple[str, str], Tuple[int, str], Tuple[str, int]], font: str, color: Tuple[int, int, int, int], weight: int = 400, size: int = 18):
        self.text = text
        self.position = position
        self.font = font
        self.color = color
        self.weight = weight
        self.size = size
    
    def __repr__(self):
        return f"<TextOperation text={self.text} position={self.position} font={self.font} color={self.color} weight={self.weight}>"
    
    def execute(self, image: PILImage.Image):
        # print("Executing text operation")
        return add_text(image,
                        self.text,
                        self.position,
                        self.font,
                        self.color,
                        self.weight,
                        self.size )