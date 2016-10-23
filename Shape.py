from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    def __init__(self):
        pass
    
    def draw(self):
        self.painter.draw()

    def set_painter(self, painter):
        self.painter = painter

    @abstractmethod
    def set_gravitycenter(self, center):
        pass

    @abstractmethod
    def gravity_center(self):
        pass



