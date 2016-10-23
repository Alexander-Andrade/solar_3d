from Shape import Shape
from Orbit import Orbit


class System:

    def __init__(self, master):
        self.master = master
        self.orbits = []
        self.satellites = []
        self.subsystems = []

    def add_satellite(self, satellite, orbit_center, orbit_radius, orbit_time):
        self.satellites.append(satellite)
        orbit = Orbit(self.master, satellite, orbit_center, orbit_radius, orbit_time)
        self.orbits.append(orbit)

    def update_state(self):
        for orbit in self.orbits:
            orbit.update_slave_position()
