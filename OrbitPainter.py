from Painter import *
from Texture import Texture2D
import math

class OrbitPainter(Painter):

    def __init__(self, orbit):
        self.orbit = orbit

    def draw(self):
        glPushAttrib(GL_CURRENT_BIT)
        glBegin(GL_POINTS)
        glColor3f(1., 1., 1.)
        # loop round from 0 to 2*PI and draw around the radius of the orbit using trigonometry
        angle = 0.0
        while angle < 6.283185307:
            glVertex3f(math.sin(angle)*self.orbit.radius, math.cos(angle)*self.orbit.radius, 0.0)
            angle += 0.05
        glVertex3f(0.0, self.orbit.radius, 0.0)
        glEnd()
        glPopAttrib()
