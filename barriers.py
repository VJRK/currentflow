import pygame
import globalvalues as gv


class Barrier(object):
    instances = []
    ramps = []

    def __init__(self,
                 typ=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        self.typ = typ
        if self.typ == "RampL" or self.typ == "RampR":
            Barrier.ramps.append(self)
        else:
            Barrier.instances.append(self)
        self.rect = pygame.Rect(x_left * gv.scale, y_top * gv.scale, width * gv.scale, height * gv.scale)

    @staticmethod
    def render(window,
               color=(255, 255, 255)):
        for barrier in Barrier.instances:
            if barrier.typ == "Wall":
                pygame.draw.rect(window, color, (barrier.rect.x, barrier.rect.y,
                                                 barrier.rect.width, barrier.rect.height))
        for ramp in Barrier.ramps:
            if ramp.typ == "RampR":
                pygame.draw.polygon(window, color, ((ramp.rect.x, ramp.rect.y + ramp.rect.height-1), (ramp.rect.x + ramp.rect.width-1, ramp.rect.y), (ramp.rect.x + ramp.rect.width-1, ramp.rect.y + ramp.rect.height-1)))
            elif ramp.typ == "RampL":
                pygame.draw.polygon(window, color, ((ramp.rect.x + ramp.rect.width-1, ramp.rect.y + ramp.rect.height-1), (ramp.rect.x, ramp.rect.y), (ramp.rect.x, ramp.rect.y + ramp.rect.height-1)))
