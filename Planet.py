from Globe import Globe
from GlobePainters import PlanetPainter, RingedPlanetPainter
from Ring import Ring
import numpy as np


class Planet(Globe):

    def __init__(self, center, radius, rotation_time, img_name, rot=np.array([0., 0., 1.0])):
        Globe.__init__(self, center, radius, rotation_time, rot)
        self.painter = PlanetPainter(self, img_name)


class RingedPlanet(Globe):

    def __init__(self, center, radius, rotation_time, img_name, ring, rot=np.array([0., 0., 1.0])):
        Globe.__init__(self, center, radius, rotation_time, rot)
        self.ring = ring
        self.painter = RingedPlanetPainter(self, img_name)

    def set_ring(self, ring):
        self.ring = ring
