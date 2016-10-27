from Globe import Globe
from GlobePainters import PlanetPainter, RingedPlanetPainter
from Ring import Ring


class Planet(Globe):

    def __init__(self, center, radius, rotation_time, img_name):
        Globe.__init__(self, center, radius, rotation_time)
        self.painter = PlanetPainter(self, img_name)


class RingedPlanet(Globe):

    def __init__(self, center, radius, rotation_time, img_name, ring):
        Globe.__init__(self, center, radius, rotation_time)
        self.ring = ring
        self.painter = RingedPlanetPainter(self, img_name)

    def set_ring(self, ring):
        self.ring = ring
