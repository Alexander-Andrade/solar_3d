from Shape import Shape
import pyassimp as assimp
from OpenGL.GL import *
import numpy as np

def gl_face_mode(face):
    n_indices = len(face)
    if n_indices == 1:
        return GL_POINTS
    elif n_indices == 2:
        return GL_LINES
    elif n_indices == 3:
        return GL_TRIANGLES
    elif n_indices == 4:
        return GL_POLYGON

from ModelPainter import ModelPainter

class Model(Shape):

    def __init__(self, model_name, center=np.array([0., 0., 0.]), scale=np.array([1., 1., 1.])):
        self.center = center
        self.scale = scale
        self.scene = assimp.load(model_name)
        self.painter = ModelPainter(self)

    def load(self, model_name):
        self.scene = assimp.load(model_name)

    def copy(self, center, scale):


    def __del__(self):
        assimp.release(self.scene)

    def set_gravitycenter(self, center):
        self.center = center

    def gravity_center(self):
        return self.center

