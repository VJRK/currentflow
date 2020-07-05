import pygame
import globalvalues as gv


class Block(object):

    def __init__(self, typ=0, x_left=None, y_top=None, width=1, height=1, color=(255, 255, 255)):
        self.typ = typ  # 0 = Wall, 1 = RampR, 2 = RampL
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)
        self.color = color
