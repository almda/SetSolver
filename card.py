from enum import Enum

class Color (Enum):
    RED = 1
    GREEN = 2
    PURPLE = 3

class Shape (Enum):
    RHOMBUS = 1
    WAVE = 2
    ELLIPSE = 3

class Filling (Enum):
    EMPTY = 1
    LINES = 2
    FULL = 3

class Card:
    def __init__(self, color, shape, filling, count):
        self.color = color
        self.shape = shape
        self.filling = filling
        self.count = count

    def __eq__(self, other):
        if(self.color == other.color and self.shape == other.shape and self.filling == other.filling
        and self.count == other.count):
            return True
        return False

    def PrintMe (self):
        print(f"Color: {self.color} Shape: {self.shape} Filling: {self.filling} Count: {self.count}")