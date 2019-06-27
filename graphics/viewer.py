"""
2D rendering framework
"""

import pyglet
from pyglet.gl import *

class Viewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width=width, height=height)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def close(self):
        self.window.close()

    def render(self, return_rgb_array=False):
        glClearColor(1,1,1,1)
        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()
        self.window.flip()

    def __del__(self):
        self.close()

viewer = Viewer(600,400)

for i in range(100):
    viewer.render()
    print(i)

viewer.close()