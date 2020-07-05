import pygame


class Block(object):

    def __init__(self, typ=0, x_left=None, y_top=None, width=1, height=1, color=(255, 255, 255)):
        self.typ = typ  # 0 = Wall, 1 = RampR, 2 = RampL
        self.rect = pygame.Rect(x_left * 25, y_top * 25, width * 25, height * 25)
        self.color = color
