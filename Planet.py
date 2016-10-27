from Globe import Globe
from GlobePainters import PlanetPainter, RingedPlanetPainter
from Ring import Ring
import numpy as np


class Planet(Globe):

    def __init__(self, center, radius, img_name, rot=None):
        Globe.__init__(self, center, radius, rot)
        self.painter = PlanetPainter(self, img_name)


class RingedPlanet(Globe):

    def __init__(self, center, radius, img_name, ring, rot=None):
        Globe.__init__(self, center, radius, rot)
        self.ring = ring
        self.painter = RingedPlanetPainter(self, img_name)

    def set_ring(self, ring):
        self.ring = ring
