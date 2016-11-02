from Painter import *
from Model import gl_face_mode
import pyassimp as assimp
import numpy as np
import copy


class ModelPainter(Painter):

    def __init__(self, model):
        self.model = model
        self.scene_list = None
        self.__compile()

    def clone(self, model):
        model_painter = copy.copy(self)
        model_painter.model = model
        return model_painter

    def __compile(self):
        self.scene_list = glGenLists(1)
        glNewList(self.scene_list, GL_COMPILE)
        self.recursive_render(self.model.scene.rootnode)
        glEndList()

    def recursive_render(self, node):
        print(node)
        glEnable(GL_TEXTURE_2D)
        glPushMatrix()
        glMultMatrixf(node.transformation)
        # draw all meshes assigned to this node
        for mesh in node.meshes:
            # apply material
            glEnable(GL_LIGHTING) if len(mesh.normals) else glDisable(GL_LIGHTING)

            for face in mesh.faces:
                face_mode = gl_face_mode(face)

                glBegin(face_mode)

                for ind in face:
                    if len(mesh.colors):
                        glColor4fv(mesh.colors[ind])
                    if len(mesh.normals):
                        glNormal3fv(mesh.normals[ind])
                    glVertex3fv(mesh.vertices[ind])
                glEnd()
        # draw all children
        for child in node.children:
            self.recursive_render(child)
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)

    def draw(self):
        glPushMatrix()
        glColor3ub(156, 73, 73)
        center = self.model.center
        scale = self.model.scale
        if self.model.rot:
            rot_axes = self.model.rot.axes
            glRotatef(self.model.rot.angle, rot_axes[0], rot_axes[1], rot_axes[2])
        glTranslatef(center[0], center[1], center[2])
        glScalef(scale[0], scale[1], scale[2])
        glCallList(self.scene_list)
        glPopMatrix()

