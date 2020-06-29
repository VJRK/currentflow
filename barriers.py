import pygame
import globalvalues as gv


class Barrier(object):
    instances = []

    def __init__(self,
                 typ=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        self.typ = typ
        Barrier.instances.append(self)
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)

    @staticmethod
    def render_barriers(window,
                        image=None,
                        color=(255, 255, 255)):
        for barrier in Barrier.instances:
            if barrier.typ == "Edge":
                window.blit(image, barrier.rect)
            elif barrier.typ == "Blank":
                pygame.draw.rect(window, color, (gv.L + barrier.rect[0], gv.T + barrier.rect[1],
                                                 barrier.rect[2], barrier.rect[3], ))
