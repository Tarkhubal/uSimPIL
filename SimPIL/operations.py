from PIL import Image as PILImage
from typing import List, Union

from .utils import round_corners

class Operation:
    def __init__(self):
        pass
    
    def execute(self, image: PILImage.Image):
        pass
    
    def __repr__(self):
        return f"<Operation>"


class RoundCornersOperation(Operation):
    def __init__(self, radius: int, corners: List[bool]):
        self.radius = radius
        self.corners = corners
    
    def __repr__(self):
        return f"<RoundCornersOperation radius={self.radius} corners={self.corners}>"
    
    def execute(self, image: PILImage.Image):
        print("Executing corners operation")
        return round_corners(image, self.radius, self.corners)

class SquareCornersOperation(Operation):
    def __init__(self, corners: int):
        self.corners = corners
    
    def __repr__(self):
        return f"<SquareCornersOperation corners={self.corners}>"
    
    def execute(self, image: PILImage.Image):
        print("Executing corners operation")
        return round_corners(image, 0, self.corners)
    