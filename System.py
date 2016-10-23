from Shape import Shape
from Orbit import Orbit
from SystemPainter import SystemPainter


class System:

    def __init__(self, master=None):
        self.master = master
        self.orbits = []
        self.satellites = []
        self.subsystems = []
        self.painter = SystemPainter(self)

    def set_master(self, master):
        self.master = master

    def add_satellite(self, satellite, orbit_radius, orbit_time):
        self.satellites.append(satellite)
        orbit = Orbit(self.master, satellite, orbit_radius, orbit_time)
        self.orbits.append(orbit)

    def append_subsystem(self, subsystem):
        self.subsystems.append(subsystem)

    def update_state(self, time):
        for orbit in self.orbits:
            orbit.update_slave_position(time)
        for satellite in self.satellites:
            satellite.calc_rotation(time)
        for subsystem in self.subsystems:
            subsystem.update_state()

    def draw(self):
        self.painter.draw()
