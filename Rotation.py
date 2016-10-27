from Painter import *
import numpy as np
from enum import Enum, unique


class Rotation:
    @unique
    class Direction(Enum):
        Left = 1
        Right = 2

    def __init__(self, angle=0, axes=np.array([0., 0., 1.0]), time=0.0, direct=Direction.Left):
        self.time = time
        self.direct = direct
        # angle in degrees
        self.angle = angle
        self.axes = axes

    def rotate_matrix(self):
        glRotatef(self.angle, self.axes[0], self.axes[1], self.axes[2])

    def update_angle(self, global_time):
        if not self.time == 0:
            if self.direct == Rotation.Direction.Right:
                self.angle = global_time * 360 / self.time
            else:
                self.angle = -global_time * 360 / self.time
