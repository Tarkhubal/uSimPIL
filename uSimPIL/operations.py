from PIL import Image as PILImage
from typing import List, Union

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
    