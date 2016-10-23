from Shape import Shape
import numpy as np


class Globe(Shape):

    def __init__(self, center, radius, rotation_time=0.0):
        self.center = center
        self.radius = radius
        # its rotation around its axis
        self.rotation = 0.0
        # time it takes to spin 360 degrees
        self.rotation_time = rotation_time

    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return self.center

    # find the rotation of the planet around its axis
    def calc_rotation(self, time):
        self.rotation = time*360/self.rotation_time



