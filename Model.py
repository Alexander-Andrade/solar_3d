from Shape import Shape
import pyassimp as assimp
from OpenGL.GL import *
import numpy as np
import copy

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

    def __init__(self, model_name, center, scale, rot=None):
        self.scene = assimp.load(model_name)
        Shape.__init__(self, center=center, scale=scale, rot=rot, painter=ModelPainter(self))

    # all the changes in the scene will effects on every clone
    def clone(self, center, scale=None, rot=None):
        clone = copy.copy(self)
        clone.center = center
        if scale:
            clone.scale = scale
        if rot:
            clone.rot = rot
        return clone

    def __del__(self):
        if self.scene:
            assimp.release(self.scene)


