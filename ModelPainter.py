from Painter import *
from Model import gl_face_mode
import pyassimp as assimp
import numpy as np


class ModelPainter(Painter):

    def __init__(self, model, scale=np.array([1., 1., 1.])):
        self.model = model
        self.scale = scale
        self.scene_list = glGenLists(1)
        glNewList(self.scene_list, GL_COMPILE)
        self.recursive_render(self.model.scene.rootnode)
        glEndList()

    def recursive_render(self, node):
        print(node)
        glEnable(GL_TEXTURE_2D)
        glPushMatrix()
        glMultMatrixf(node.transformation)
        meshes = self.model.scene
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
        center = self.model.center
        glTranslatef(center[0], center[1], center[2])
        glScalef(self.scale[0], self.scale[1], self.scale[2])
        glCallList(self.scene_list)
        glPopMatrix()

