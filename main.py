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


class Window:

    def __init__(self, application, **kwargs):
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
        glEnable(GL_DEPTH_TEST)
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
        self.time_speed = 0.1
        self.timer = Timer(10, True)

        self.solar_system = None
        self.background_painter = None
        self.camera = Camera()
        self.key_controls = {b'w': Camera.CameraState.Forward,
                             b'a': Camera.CameraState.Left,
                             b'd': Camera.CameraState.Forward,
                             b's': Camera.CameraState.Backward,
                             b'l': Camera.CameraState.RollRight,
                             b'j': Camera.CameraState.RollLeft,
                             b'i': Camera.CameraState.RollRight,
                             b'k': Camera.CameraState.RollRight,
                             b'q': Camera.CameraState.YawLeft,
                             b'e': Camera.CameraState.YawRight,
                             }

    def init_solar_system(self):
        self.background_painter = BackgroundPainter('images/space2.jpg')
        self.solar_system = System(Star(np.array([0., 0., 0.]), 0.3, 0.001, 'images/globes/sun.jpg'))
        mars = Planet(np.array([0.2, 0.2, 0.2]), 0.03, 0.1, 'images/globes/mars.jpg')
        self.solar_system.add_satellite(mars, 0.5, 4000)

    def start_timer(self):
        self.timer.start(self.on_timer)
        self.camera.move()

    def on_timer(self):
        # update the logic and simulation
        self.time += self.time_speed
        self.solar_system.update_state(self.time)
        glutPostRedisplay()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # set up the perspective matrix for rendering the 3d world
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(70.0, self.window.width()/self.window.height(),0.001, 500.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # perform the camera orientation transform
        self.camera.transform_orientation()
        self.camera.transform_translation()
        # draw the skybox
        self.background_painter.draw()
        self.solar_system.draw()

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
    app = Application()
    window = Window(app)
    app.window = window
    app.init_solar_system()
    window.main_loop()



