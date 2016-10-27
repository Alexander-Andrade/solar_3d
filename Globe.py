from Shape import Shape
from Rotation import Rotation
import numpy as np


class Globe(Shape):

    def __init__(self, center, radius, rot=None):
        self.center = center
        self.radius = radius
        # its rotation around its axis
        self.rot = rot


    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return self.center




