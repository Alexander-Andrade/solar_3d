from Shape import Shape
from RingPainter import RingPainter
import numpy as np


class Ring(Shape):

    def __init__(self, inner_radius, outer_radius, img_name, rot_angle=0.0, rot=np.zeros(4), center=None):
        self.center = center
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.rot_angle = rot_angle
        self.rot = rot
        self.painter = RingPainter(self, img_name)

    def set_rotation(self, rot_angle, rot):
        self.rot_angle = rot_angle
        self.rot = rot

    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return  self.center