from Globe import Globe
from Painter import StarPainter

class Star(Globe):

    def __init__(self, center, radius, rotation_time, img_name):
        Globe.__init__(self, center, radius, rotation_time)
        self.painter = StarPainter(self, img_name)
