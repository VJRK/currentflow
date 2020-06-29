import pygame
import globalvalues as gv

class Barrier(object):
    instances = []

    def __init__(self,
                 type=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        self.type = type
        Barrier.instances.append(self)
        self.rect = pygame.Rect(x_left * gv.scale, y_top * gv.scale, width * gv.scale, height * gv.scale)

    @staticmethod
    def render_barriers(window,
                        image=None,
                        color=(255, 255, 255)):
        for barrier in Barrier.instances:
            if barrier.type == "Edge":
                window.blit(image, barrier.rect)
            elif barrier.type == "Blank":
                pygame.draw.rect(window, color, barrier.rect)
