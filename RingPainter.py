from Painter import *
from Texture import Texture2D


class RingPainter(Painter):

    def __init__(self, ring, img_name):
        self.ring = ring
        self.slices = 30
        self.loops = 30
        self.texture = Texture2D(img_name)

    def draw(self):
        glPushAttrib(GL_ENABLE_BIT) #to enable and disable texturing
        glPushMatrix()
        self.texture.bind_texture()
        rot = self.ring.rot
        glRotatef(self.ring.rot_angle, rot[0], rot[1], rot[2])
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, True)
        gluQuadricNormals(quadric, GLU_SMOOTH)
        gluDisk(quadric, self.ring.inner_radius, self.ring.outer_radius, self.slices, self.loops)
        glPopMatrix()
        glPopAttrib()
