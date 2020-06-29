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
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)

    @staticmethod
    def render(window,
               image=None,
               color=(255, 255, 255)):
        for barrier in Barrier.instances:
            if barrier.typ == "Edge":
                window.blit(image, barrier.rect)
            elif barrier.typ == "Wall":
                pygame.draw.rect(window, color, (gv.L + barrier.rect[0], gv.T + barrier.rect[1],
                                                 barrier.rect[2], barrier.rect[3]))
        for ramp in Barrier.ramps:
            if ramp.typ == "RampR":
                pygame.draw.polygon(window, color, ((gv.L + ramp.rect[0], gv.T + ramp.rect[1] + 24), (gv.L + ramp.rect[0] + 24, gv.T + ramp.rect[1]), (gv.L + ramp.rect[0] + 24, gv.T + ramp.rect[1] + 24)))
            elif ramp.typ == "RampL":
                pygame.draw.polygon(window, color, ((gv.L + ramp.rect[0] + 24, gv.T + ramp.rect[1] + 24), (gv.L + ramp.rect[0], gv.T + ramp.rect[1]), (gv.L + ramp.rect[0], gv.T + ramp.rect[1] + 24)))
