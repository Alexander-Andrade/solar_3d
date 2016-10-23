from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from System import System
from Camera import Camera
from Timer import Timer
from BackgroundPainter import BackgroundPainter


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
        print(glutGet(GLUT_SCREEN_WIDTH))

    def width(self):
        return self.win_size[0]

    def height(self):
        return self.win_size[1]

    def __gl_init(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def __init_lightning(self):
        # color search
        glEnable(GL_COLOR_MATERIAL)
        #glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glEnable(GL_NORMALIZE)

    def __register_event_handlers(self):
        glutDisplayFunc(self.application.display)
        glutReshapeFunc(Window.reshape)
        glutKeyboardFunc(self.application.key_down)
        glutKeyboardUpFunc(self.application.key_up)

    def main_loop(self):
        glutMainLoop()

    def reshape(self, w, h):
        self.win_size[0] = w
        self.win_size[1] = h
        glViewport(0, 0, w, h)


class Application:

    def __init__(self):
        self.window = None

        self.time = None
        self.time_speed = None
        self.timer = Timer(10, True)

        self.sun = None
        self.solar_system = System(self.sun)
        self.background_painter = BackgroundPainter('path_to_background')
        self.camera = Camera()

    def start_timer(self):
        self.timer.start(self.on_timer)

    def on_timer(self):
        # update the logic and simulation
        self.time += self.time_speed


    def create_shapes(self):
        pass

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
        # draw the skybox
        self.background_painter.draw()
        self.camera.transform_translation()



        glFlush()
        glutSwapBuffers()

    def key_down(self, key, x, y):
        print("down: {}, {}, {}".format(key, x, y))

    def key_up(self, key, x, y):
        print("up: {}, {}, {}".format(key, x, y))



if __name__ == "__main__":
    glutInit(sys.argv)
    app = Application()
    window = Window(app)
    app.window = window

    window.main_loop()



