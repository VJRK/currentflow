import pygame
import globalvalues as gv


class Fluid(object):
    instances = []

    def __init__(self,
                 typ=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=.7):
        self.typ = typ
        Fluid.instances.append(self)
        y_top = y_top + .2
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)

    @staticmethod
    def render(window,
               image=None,
               color=(255, 255, 255)):
        for fluid in Fluid.instances:
            if fluid.typ == "electricity":
                pygame.draw.rect(window, (255, 255, 0), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))
            elif fluid.typ == "water":
                pygame.draw.rect(window, (0, 255, 255), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))
            elif fluid.typ == "acid":
                pygame.draw.rect(window, (0, 255, 0), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))
