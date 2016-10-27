from Painter import *
import numpy as np


class Rotation:

    def __init__(self, angle=0, axes=np.array([0., 0., 1.0]), time=0.0):
        self.time = time
        # angle in degrees
        self.angle = angle
        self.axes = axes

    def rotate_matrix(self):
        glRotatef(self.angle, self.axes[0], self.axes[1], self.axes[2])

    def update_angle(self, global_time):
        if not self.time == 0:
            self.angle = global_time * 360 / self.time
