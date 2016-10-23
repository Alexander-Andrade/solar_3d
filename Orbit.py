from Shape import Shape
import numpy as np
import math


class Orbit(Shape):

    def __init__(self, master_shape, slave_shape, center, radius, orbit_time):
        self.center = center
        self.master_shape = master_shape
        self.slave_shape = slave_shape
        self.radius = radius
        # time it takes to complete 1 orbit
        self.orbit_time = orbit_time

    # Calculate its position in 3d spacein the orbit using the given time value
    def update_slave_position(self, time):
        angle = time*math.pi/self.orbit_time
        slave_center = np.zeros(3)
        slave_center[0] = math.sin(angle)*self.radius
        slave_center[1] = math.cos(angle)*self.radius
        slave_center[2] = 0
        self.slave_shape.set_gravitycenter(slave_center)

    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return self.center
