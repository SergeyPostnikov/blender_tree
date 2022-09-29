from matrix_functions import rotate_x, rotate_y, rotate_z
import numpy as np

class BaseFigure:
    def __init__(self, verts):
        self.verts = verts
        self.scale = 1

    def get_verts(self):
        return (vert * self.scale for vert in self.verts)

    def rotate(self, angle):
        self.verts = self.verts @ rotate_x(angle)


