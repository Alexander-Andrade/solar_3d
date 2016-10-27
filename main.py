from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from System import System
from Camera import Camera
from Timer import Timer
from BackgroundPainter import BackgroundPainter
from Star import Star
from Planet import Planet, RingedPlanet
from Ring import Ring
from Rotation import Rotation
import numpy as np
# import pyassimp as assimp
# import pyglet
class Window:

    def __init__(self, application, **kwargs):
        self.win_size = (0, 0)
        self.application = application
        self.__init_window(**kwargs)
        self.__init_lightning()
        self.__gl_init()
        self.__register_event_handlers()

    def __init_window(self, win_pos=(100, 100), title='window', win_size=(600, 600),
                      display_mode=GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH):
        self.win_size = win_size
        glutInitDisplayMode(display_mode)
        glutInitWindowSize(win_size[0], win_size[1])
        glutInitWindowPosition(win_pos[0], win_pos[1])
        glutCreateWindow(title)

    def width(self):
        return self.win_size[0]

    def height(self):
        return self.win_size[1]

    def __gl_init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_SMOOTH)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def __init_lightning(self):
        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        mat_specular = np.array([1.0, 1.0, 1.0, 1.0])
        mat_ambience = np.array([0.6, 0.6, 0.6, 1.0])
        mat_shininess = np.array([40.0])

        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambience)

    def __register_event_handlers(self):
        glutDisplayFunc(self.application.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.application.key_down)
        glutKeyboardUpFunc(self.application.key_up)

    def main_loop(self):
        glutMainLoop()

    def reshape(self, w, h):
        self.win_size = w, h
        glViewport(0, 0, w, h)


class Application:

    def __init__(self):
        self.window = None

        self.time = 2.552
        self.time_speed = 0.5
        self.timer = Timer(10, True)

        self.solar_system = None
        self.background_painter = None
        self.camera = Camera()
        self.key_controls = {b'w': Camera.CameraState.Forward,
                             b'a': Camera.CameraState.Left,
                             b'd': Camera.CameraState.Right,
                             b's': Camera.CameraState.Backward,
                             b'l': Camera.CameraState.RollRight,
                             b'j': Camera.CameraState.RollLeft,
                             b'i': Camera.CameraState.PitchDown,
                             b'k': Camera.CameraState.PitchUp,
                             b'q': Camera.CameraState.YawLeft,
                             b'e': Camera.CameraState.YawRight,
                             }

    def init_solar_system(self):
        self.background_painter = BackgroundPainter('images/space5.png')

        solar_rotation = Rotation(angle=0, axes=np.array([0., 0., 1.0]), time=5000)
        self.solar_system = System(master=Star(center=np.array([0., 0., 0.]), radius=0.6, img_name='images/globes/sun.jpg', rot=solar_rotation))

        mercury_rotation = Rotation(angle=7, axes=np.array([0., 0., 1.0]), time=10)
        mercury = Planet(center=np.array([0., 0., 0.]), radius=0.05, img_name='images/globes/mercury.jpg', rot=mercury_rotation)
        self.solar_system.add_satellite(satellite=mercury, orbit_radius=0.7, orbit_time=400, init_orbit_angle=1.1)

        venus_rotation = Rotation(angle=3, axes=np.array([0., 0., 1.0]), time=3000)
        venus = Planet(center=np.array([0., 0., 0.]), radius=0.06, img_name='images/globes/venus.jpg', rot=venus_rotation)
        self.solar_system.add_satellite(satellite=venus, orbit_radius=1.3, orbit_time=600, init_orbit_angle=0.5)

        earth_rotation = Rotation(angle=23, axes=np.array([0., 0., 1.0]), time=300)
        earth = Planet(center=np.array([0., 0., 0.]), radius=0.06, img_name='images/globes/earth.jpg', rot=earth_rotation)
        earth_subsystem = System(earth)
        moon = Planet(center=np.array([0., 0., 0.]), radius=0.01, img_name='images/globes/moon.jpg')
        earth_subsystem.add_satellite(satellite=moon, orbit_radius=0.1, orbit_time=200)
        self.solar_system.append_subsystem(subsystem=earth_subsystem, orbit_radius=2.3, orbit_time=900, init_orbit_angle=2.3)

        mars_rotation = Rotation(angle=25, axes=np.array([0., 0., 1.0]), time=301)
        mars = Planet(center=np.array([0., 0., 0.]), radius=0.04, img_name='images/globes/mars.jpg',rot=mars_rotation)
        self.solar_system.add_satellite(mars, 3.0, 1200, 3.1)

        ganimede = Planet(np.array([0., 0., 0.]), 0.03, 'images/globes/ganimede.jpg')
        upiter_rotation = Rotation(angle=3, axes=np.array([0., 0., 1.0]), time=200)
        upiter = Planet(np.array([0., 0., 0.]), 0.2, 'images/globes/upiter.jpg', rot=upiter_rotation)
        upiter_subsystem = System(upiter)
        upiter_subsystem.add_satellite(satellite=ganimede, orbit_radius=0.3, orbit_time=200)
        self.solar_system.append_subsystem(subsystem=upiter_subsystem, orbit_radius=6.0, orbit_time=6000, init_orbit_angle=1.3)
        #self.solar_system.add_satellite(satellite=upiter, orbit_radius=6.0, orbit_time=6000, init_orbit_angle=1.3)

        saturn_rotation = Rotation(angle=26, axes=np.array([0., 0., 1.0]), time=200)
        saturn_ring = Ring(center=np.array([0., 0., 0.]), inner_radius=0.23, outer_radius=0.4, img_name='images/globes/saturn_ring2.png')
        saturn = RingedPlanet(center=np.array([0., 0., 0.]),radius=0.19, img_name='images/globes/saturn.jpg', ring=saturn_ring, rot=saturn_rotation)
        self.solar_system.add_satellite(satellite=saturn, orbit_radius=7.0, orbit_time=6500, init_orbit_angle=3.4)

        uranus_rotation = Rotation(angle=82, axes=np.array([0., 0., 1.0]), time=200)
        uranus_ring = Ring(center=np.array([0., 0., 0.]), inner_radius=0.23, outer_radius=0.4,
                           img_name='images/globes/uranus_ring.png')
        uranus = RingedPlanet(center=np.array([0., 0., 0.]), radius=0.19, img_name='images/globes/uranus.jpg', ring=uranus_ring, rot=uranus_rotation)
        self.solar_system.add_satellite(satellite=uranus, orbit_radius=8.2, orbit_time=8000, init_orbit_angle=2.624)

        neptune_rotation = Rotation(angle=29, axes=np.array([0., 0., 1.0]), time=200)
        neptune = Planet(center=np.array([0., 0., 0.]), radius=0.19, img_name='images/globes/neptune.jpg', rot=neptune_rotation)
        self.solar_system.add_satellite(satellite=neptune, orbit_radius=12.2, orbit_time=10000, init_orbit_angle=1.8)

    def start_timer(self):
        self.timer.start(self.on_timer)

    def on_timer(self):
        self.camera.move()
        # update the logic and simulation
        self.time += self.time_speed
        self.solar_system.update_state(self.time)
        glutPostRedisplay()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # set up the perspective matrix for rendering the 3d world
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70.0, self.window.width()/self.window.height(), 0.001, 5000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # perform the camera orientation transform
        self.camera.transform_orientation()

        # draw the skybox
        self.background_painter.draw()
        self.camera.transform_translation()
        glEnable(GL_DEPTH_TEST) # use z-test only for models not for skybox
        self.solar_system.draw()
        glDisable(GL_DEPTH_TEST)

        glFlush()
        glutSwapBuffers()

    def key_down(self, key, x, y):
        try:
            state = self.key_controls[key]
            self.camera.add_state(state)
        except KeyError as e:
            print(e)

    def key_up(self, key, x, y):
        try:
            state = self.key_controls[key]
            self.camera.del_state(state)
        except KeyError as e:
            print(e)


if __name__ == "__main__":
    glutInit(sys.argv)
    # falcon = assimp.load('models/star_wars_falcon/star_wars_falcon.3ds')
    # print(len(falcon.meshes))
    # print(len(falcon.mesh[0].vertices))
    # print(falcon.mesh[0].vertices)
    app = Application()
    window = Window(app)
    app.window = window
    app.init_solar_system()
    app.start_timer()
    window.main_loop()


