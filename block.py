import pygame

import globalvalues as gv


class Block(object):

    def __init__(self, typ=0, x_left=None, y_top=None, width=1, height=1, color=(255, 255, 255)):
        self.typ = typ  # 0 = Wand, 1 = RampeR, 2 = RampeL, 3 = Halber Block, 4 = Ziel Current, 5 = Ziel Flow
        self.rect = pygame.Rect(x_left * gv.sc, y_top * gv.sc, width * gv.sc, height * gv.sc)
        self.color = color
