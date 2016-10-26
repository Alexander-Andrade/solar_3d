from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from System import System
from Camera import Camera
from Timer import Timer
from BackgroundPainter import BackgroundPainter
from Star import Star
from Planet import Planet
from Orbit import Orbit
import numpy as np
import pyassimp as assimp

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
        glEnable(GL_TEXTURE_2D)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def __init_lightning(self):
        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        mat_specular = np.array([1.0, 1.0, 1.0, 1.0])
        mat_ambience = np.array([0.3, 0.3, 0.3, 1.0])
        mat_shininess = np.array([20.0])

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

        self.solar_system = System(Star(np.array([0., 0., 0.]), 0.3, 0.1, 'images/globes/sun.jpg'))
        mercury = Planet(np.array([0., 0., 0.]), 0.06, 0.1, 'images/globes/mercury.jpg')
        self.solar_system.add_satellite(mercury, 0.5, 4000)

        # earth = Planet(np.array([0., 0., 0.]), 0.09, 0.1, 'images/globes/earth.jpg')
        # earth_subsystem = System(earth)
        # moon = Planet(np.array([0., 0., 0.]), 0.005, 0.1, 'images/globes/moon.jpg')
        # earth_subsystem.add_satellite(moon, 0.1, 200)
        # self.solar_system.append_subsystem(earth_subsystem, 0.6, 5000)

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



