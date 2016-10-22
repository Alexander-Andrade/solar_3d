import numpy as np


# camera is an observer
# so the keyboard would manipulate roll and direction and move around
# so im representing it with 4 vectors
# an up, forward, and right vector to represent orientation on all axes
# and a position vector to represent the translation

class Camera:

    def __init__(self):
        # a vector pointing to the direction you're facing
        self.forward_vec = np.zeros(3)
        # a vector pointing to the right of where you're facing
        self.right_vec = np.zeros(3)
        self.up_vec = np.zeros(3)
        # a vector describing the position of the camera
        self.pos_vec = np.array({})
        #the camera speed
        self.speed = 0.005
        self.turn_speed = 0.01

    # transform the opengl view matrix for the orientation
    def transform_orientation(self):
        pass

    # transform the opoengl view matrix for the translation
    def transform_translation(self):
        pass

    # points the camera at the given point in 3d space
    def point_at(self):
        pass

    # speed up the camera speed
    def speed_up(self):
        pass

    # slow down the camera speed
    def slow_down(self):
        pass

    # move the camera forward
    def move_forward(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_backward(self):
        pass

    def roll_right(self):
        pass

    def roll_left(self):
        pass

    def pitch_up(self):
        pass

    def pitch_down(self):
        pass

    def yaw_left(self):
        pass

    def yaw_right(self):
        pass

