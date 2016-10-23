from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2 as cv
import numpy as np


class Texture2D:

    def __init__(self, image_name, img_format=GL_RGB):
        self.image = cv.imread(image_name, cv.IMREAD_UNCHANGED)
        self.width, self.height, self.bytes_per_pix = self.image.shape
        self.image = np.reshape(self.image, (self.width*self.height, self.bytes_per_pix))
        self.img_format = self.__get_gl_img_format(image_name)

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        gluBuild2DMipmaps(GL_TEXTURE_2D, self.img_format, self.width, self.height, self.img_format, GL_UNSIGNED_BYTE, self.image)

    def __get_gl_img_format(self, image_name):
        if image_name.endswith('jpg') and self.bytes_per_pix == 3:
            return GL_RGB
        elif image_name.endswith('png') and self.bytes_per_pix == 4:
            return GL_RGBA

    def bind_texture(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
