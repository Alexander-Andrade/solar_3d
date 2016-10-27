from Shape import Shape
from RingPainter import RingPainter
from Rotation import Rotation
import numpy as np


class Ring(Shape):

    def __init__(self, center, inner_radius, outer_radius, img_name, rot=None):
        self.center = center
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.rot = rot
        self.painter = RingPainter(self, img_name)

    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return  self.center