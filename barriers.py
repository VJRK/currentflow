import pygame
import globalvalues as gv
import math


class Barrier(object):
    instances = []
    ramps = []

    def __init__(self, typ=None, x_left=None, y_top=None, width=1, height=1, color=(255, 255, 255)):
        self.typ = typ
        self.color = color
        if self.typ == "RampL" or self.typ == "RampR":
            Barrier.ramps.append(self)
        else:
            Barrier.instances.append(self)
        self.rect = pygame.Rect(x_left * 25, y_top * 25, width * 25, height * 25)

    @staticmethod
    def render(window):
        for barrier in Barrier.instances:
            if barrier.typ == "Wall":
                pygame.draw.rect(window, barrier.color, (gv.L + barrier.rect.x, gv.T + barrier.rect.y,
                                                         barrier.rect.width, barrier.rect.height))
        for ramp in Barrier.ramps:
            if ramp.typ == "RampR":
                pygame.draw.polygon(window, barrier.color, (
                    (gv.L + ramp.rect.x, gv.T + ramp.rect.y + ramp.rect.height - 1),
                    (gv.L + ramp.rect.x + ramp.rect.width - 1, gv.T + ramp.rect.y),
                    (gv.L + ramp.rect.x + ramp.rect.width - 1, gv.T + ramp.rect.y + ramp.rect.height - 1)))
            elif ramp.typ == "RampL":
                pygame.draw.polygon(window, barrier.color, (
                    (gv.L + ramp.rect.x + ramp.rect.width - 1, gv.T + ramp.rect.y + ramp.rect.height - 1),
                    (gv.L + ramp.rect.x, gv.T + ramp.rect.y),
                    (gv.L + ramp.rect.x, gv.T + ramp.rect.y + ramp.rect.height - 1)))
