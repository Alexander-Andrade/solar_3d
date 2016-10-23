from Painter import *
from Texture import Texture2D


class PlanetPainter(Painter):

    def __init__(self, planet, img_name):
        self.planet = planet
        self.texture = Texture2D(img_name)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.planet.center[0], self.planet.center[1], self.planet.center[2])
        glRotatef(self.planet.rotation, 0.0, 0.0, 1.0)
        self.texture.bind_texture()
        # render as a GLU shhere quadric object
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, True)
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluSphere(quadric, self.planet.radius, 30, 30)
        glPopMatrix()


class StarPainter(Painter):
    def __init__(self, star, img_name, light=GL_LIGHT0):
        self.star = star
        self.light = light
        self.texture = Texture2D(img_name)

    def point_light(self):
        glEnable(self.light)
        glLightfv(self.light, GL_AMBIENT, (0.3, 0.3, 0.3, 1.0))
        glLightfv(self.light, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        glLightfv(self.light, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
        glLightfv(self.light, GL_POSITION, (0.0, 0.0, 0.0, 1.0))
        glLightf(self.light, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(self.light, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(self.light, GL_QUADRATIC_ATTENUATION, 0.2)

    def draw(self):
        self.point_light()
        glPushMatrix()
        glTranslatef(self.star.center[0], self.star.center[1], self.star.center[2])
        #glRotatef(self.star.rotation, 0.0, 0.0, 1.0)
        self.texture.bind_texture()
        # render as a GLU shhere quadric object
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, True)
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluSphere(quadric, self.star.radius, 30, 30)
        glPopMatrix()
