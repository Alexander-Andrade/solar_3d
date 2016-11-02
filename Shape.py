# from abc import ABCMeta, abstractmethod
import numpy as np


class Shape:

    def __init__(self, **kwargs):
        self.center = kwargs.get("center", np.array([.0, .0, .0]))
        self.scale = kwargs.get("scale", np.array([1., 1., 1.]))
        self.rot = kwargs.get("rot", None)
        self.painter = kwargs.get("painter", None)

    def draw(self):
        self.painter.draw()




