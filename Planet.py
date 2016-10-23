from Globe import Globe
from GlobePainters import PlanetPainter


class Planet(Globe):

    def __init__(self, center, radius, rotation_time, img_name):
        Globe.__init__(self, center, radius, rotation_time)
        self.painter = PlanetPainter(self, img_name)


