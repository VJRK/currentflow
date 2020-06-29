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
        self.type = typ
        Barrier.instances.append(self)
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)

    @staticmethod
    def render(window,
               image=None,
               color=(255, 255, 255)):
        for barrier in Barrier.instances:
            if barrier.type == "Edge":
                window.blit(image, barrier.rect)
            elif barrier.type == "Blank":
                pygame.draw.rect(window, color, barrier.rect)
